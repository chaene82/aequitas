# Terraform configuration for Aequitas Google Cloud deployment

terraform {
  required_version = ">= 1.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1"
    }
  }
}

# Variables
variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The GCP zone"
  type        = string
  default     = "us-central1-a"
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "aequitas"
}

variable "db_user" {
  description = "Database user"
  type        = string
  default     = "aequitas_user"
}

# Configure the Google Cloud Provider
provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

# Enable required APIs
resource "google_project_service" "required_apis" {
  for_each = toset([
    "cloudbuild.googleapis.com",
    "run.googleapis.com",
    "sql-component.googleapis.com",
    "sqladmin.googleapis.com",
    "secretmanager.googleapis.com",
    "containerregistry.googleapis.com",
    "servicenetworking.googleapis.com"
  ])

  project = var.project_id
  service = each.value

  disable_dependent_services = false
  disable_on_destroy        = false
}

# Generate random password for database
resource "random_password" "db_password" {
  length  = 16
  special = true
}

# Generate random Django secret key
resource "random_password" "django_secret_key" {
  length  = 50
  special = true
}

# Store database password in Secret Manager
resource "google_secret_manager_secret" "db_password" {
  secret_id = "db-password"
  project   = var.project_id

  replication {
    auto {}
  }

  depends_on = [google_project_service.required_apis]
}

resource "google_secret_manager_secret_version" "db_password" {
  secret      = google_secret_manager_secret.db_password.id
  secret_data = random_password.db_password.result
}

# Store Django secret key in Secret Manager
resource "google_secret_manager_secret" "django_secret_key" {
  secret_id = "django-secret-key"
  project   = var.project_id

  replication {
    auto {}
  }

  depends_on = [google_project_service.required_apis]
}

resource "google_secret_manager_secret_version" "django_secret_key" {
  secret      = google_secret_manager_secret.django_secret_key.id
  secret_data = random_password.django_secret_key.result
}

# Create Cloud SQL instance
resource "google_sql_database_instance" "aequitas_db" {
  name             = "aequitas-db"
  project          = var.project_id
  region           = var.region
  database_version = "POSTGRES_15"

  settings {
    tier              = "db-f1-micro"
    availability_type = "ZONAL"
    
    disk_size       = 10
    disk_type       = "PD_SSD"
    disk_autoresize = true

    backup_configuration {
      enabled                        = true
      start_time                     = "03:00"
      point_in_time_recovery_enabled = true
      location                       = var.region
      
      backup_retention_settings {
        retained_backups = 7
      }
    }

    database_flags {
      name  = "cloudsql.iam_authentication"
      value = "on"
    }

    database_flags {
      name  = "log_connections"
      value = "on"
    }

    ip_configuration {
      ipv4_enabled = false
      private_network = google_compute_network.aequitas_network.id
      require_ssl = true
    }
  }

  deletion_protection = false

  depends_on = [
    google_project_service.required_apis,
    google_service_networking_connection.private_vpc_connection
  ]
}

# Create database
resource "google_sql_database" "aequitas_database" {
  name     = var.db_name
  instance = google_sql_database_instance.aequitas_db.name
  project  = var.project_id
}

# Create database user
resource "google_sql_user" "aequitas_user" {
  name     = var.db_user
  instance = google_sql_database_instance.aequitas_db.name
  password = random_password.db_password.result
  project  = var.project_id
}

# Create VPC network for private IP
resource "google_compute_network" "aequitas_network" {
  name                    = "aequitas-network"
  project                 = var.project_id
  auto_create_subnetworks = false

  depends_on = [google_project_service.required_apis]
}

# Create subnet
resource "google_compute_subnetwork" "aequitas_subnet" {
  name          = "aequitas-subnet"
  project       = var.project_id
  region        = var.region
  network       = google_compute_network.aequitas_network.id
  ip_cidr_range = "10.1.0.0/16"

  log_config {
    aggregation_interval = "INTERVAL_10_MIN"
    flow_sampling        = 0.5
    metadata             = "INCLUDE_ALL_METADATA"
  }
}

# Reserve IP range for private services
resource "google_compute_global_address" "private_ip_range" {
  name          = "aequitas-private-ip"
  project       = var.project_id
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = google_compute_network.aequitas_network.id

  depends_on = [google_project_service.required_apis]
}

# Create private connection
resource "google_service_networking_connection" "private_vpc_connection" {
  network                 = google_compute_network.aequitas_network.id
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.private_ip_range.name]

  depends_on = [google_project_service.required_apis]
}

# Create service account for Cloud Run
resource "google_service_account" "cloud_run_sa" {
  account_id   = "aequitas-cloud-run"
  display_name = "Aequitas Cloud Run Service Account"
  project      = var.project_id

  depends_on = [google_project_service.required_apis]
}

# Grant necessary permissions to service account
resource "google_project_iam_member" "cloud_run_sa_roles" {
  for_each = toset([
    "roles/cloudsql.client",
    "roles/secretmanager.secretAccessor",
    "roles/storage.objectViewer"
  ])

  project = var.project_id
  role    = each.value
  member  = "serviceAccount:${google_service_account.cloud_run_sa.email}"
}

# Outputs
output "database_instance_name" {
  description = "Cloud SQL instance name"
  value       = google_sql_database_instance.aequitas_db.name
}

output "database_connection_name" {
  description = "Cloud SQL connection name"
  value       = google_sql_database_instance.aequitas_db.connection_name
}

output "service_account_email" {
  description = "Service account email for Cloud Run"
  value       = google_service_account.cloud_run_sa.email
}

output "project_id" {
  description = "GCP Project ID"
  value       = var.project_id
}

output "region" {
  description = "GCP Region"
  value       = var.region
}
