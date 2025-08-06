# Google Cloud Deployment Guide for Aequitas

This guide provides instructions for deploying the Aequitas Django application to Google Cloud Platform using Cloud Run and Cloud SQL.

## Prerequisites

1. **Google Cloud Platform Account**: Ensure you have a GCP account with billing enabled
2. **Google Cloud SDK**: Install and configure `gcloud` CLI
3. **Terraform** (optional but recommended): For infrastructure as code
4. **Docker**: For local development and testing

## Architecture

The Google Cloud deployment consists of:

- **Cloud Run**: Serverless container hosting for the Django application
- **Cloud SQL (PostgreSQL)**: Managed database service
- **Secret Manager**: Secure storage for sensitive configuration
- **Container Registry**: Docker image storage
- **Cloud Build**: Automated CI/CD pipeline

## Quick Deployment

### 1. Automated Deployment (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd aequitas

# Run the deployment script
./deploy-gcloud.sh YOUR_PROJECT_ID us-central1
```

### 2. Manual Deployment

#### Step 1: Set up Infrastructure with Terraform

```bash
cd terraform

# Initialize Terraform
terraform init

# Copy and configure variables
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your project details

# Plan and apply infrastructure
terraform plan
terraform apply
```

#### Step 2: Build and Deploy Application

```bash
# Build and deploy using Cloud Build
gcloud builds submit \
    --config cloudbuild.yaml \
    --substitutions=_REGION=us-central1,_PROJECT_ID=YOUR_PROJECT_ID
```

## Configuration

### Environment Variables

The application uses the following environment variables for Google Cloud:

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_ENGINE` | Database engine | `django.db.backends.postgresql` |
| `DB_HOST` | Database host (Cloud SQL Unix socket) | `/cloudsql/PROJECT:REGION:INSTANCE` |
| `DB_NAME` | Database name | `aequitas` |
| `DB_USER` | Database username | `aequitas_user` |
| `DB_PASS` | Database password (from Secret Manager) | - |
| `SECRET_KEY` | Django secret key (from Secret Manager) | - |
| `DEBUG` | Debug mode | `0` |
| `ALLOWED_HOSTS` | Allowed hosts | `*` |
| `USE_GUNICORN` | Use Gunicorn server | `1` |

### Secret Manager

Sensitive configuration is stored in Google Secret Manager:

- `db-password`: PostgreSQL database password
- `django-secret-key`: Django application secret key

## Infrastructure Components

### Cloud SQL

- **Instance**: `aequitas-db`
- **Version**: PostgreSQL 15
- **Tier**: `db-f1-micro` (adjustable)
- **Features**: 
  - Automated backups
  - Point-in-time recovery
  - Private IP connectivity
  - SSL enforcement

### Cloud Run

- **Service**: `aequitas-app`
- **Region**: `us-central1` (configurable)
- **Resources**: 1 vCPU, 1GB RAM
- **Scaling**: 0-10 instances
- **Features**:
  - Health checks
  - Private VPC connectivity
  - Managed SSL certificates

### Security

- **Service Account**: Dedicated service account with minimal permissions
- **IAM Roles**:
  - `roles/cloudsql.client`
  - `roles/secretmanager.secretAccessor`
  - `roles/storage.objectViewer`
- **Network**: Private VPC with service networking

## Monitoring and Maintenance

### Health Checks

The application provides a health check endpoint:
```
GET /health/
```

### Logging

View application logs:
```bash
# Real-time logs
gcloud logs tail --service=aequitas-app

# Historical logs
gcloud logs read --service=aequitas-app --limit=100
```

### Database Management

#### Running Migrations

Migrations are automatically run during deployment. To run manually:

```bash
# Connect to Cloud Run instance
gcloud run jobs create migration-job \
    --image=gcr.io/PROJECT_ID/aequitas-app:latest \
    --set-env-vars="DB_ENGINE=django.db.backends.postgresql,..." \
    --execute-now
```

#### Database Console

```bash
# Connect to Cloud SQL instance
gcloud sql connect aequitas-db --user=aequitas_user
```

## Scaling and Performance

### Automatic Scaling

Cloud Run automatically scales based on:
- Request volume
- CPU utilization
- Memory usage

### Performance Tuning

1. **Database Connection Pooling**: Configured with `CONN_MAX_AGE=600`
2. **Static Files**: Served efficiently with WhiteNoise
3. **Gunicorn Workers**: Configured for optimal performance

## Cost Optimization

### Cloud Run Pricing

- Pay per request and compute time
- No charges when idle
- Free tier: 2 million requests/month

### Cloud SQL Pricing

- Choose appropriate machine type
- Use automatic storage scaling
- Schedule automated backups efficiently

## Troubleshooting

### Common Issues

1. **Database Connection Errors**
   - Check Cloud SQL instance status
   - Verify service account permissions
   - Check VPC connectivity

2. **Secret Manager Access**
   - Verify service account has `secretmanager.secretAccessor` role
   - Check secret names match configuration

3. **Build Failures**
   - Check Cloud Build logs
   - Verify Docker image builds locally
   - Check API enablement

### Support Resources

- **Cloud Run Documentation**: https://cloud.google.com/run/docs
- **Cloud SQL Documentation**: https://cloud.google.com/sql/docs
- **Django on Google Cloud**: https://cloud.google.com/python/django

## Development Workflow

### Local Development

For local development, continue using the existing Docker Compose setup:

```bash
# Copy environment file
cp .env.sample .env
# Edit .env with local values

# Start local environment
docker compose up
```

### Testing Deployment

Test the Google Cloud build locally:

```bash
# Build using Cloud Build locally
cloud-build-local --config=cloudbuild.yaml --dryrun=false .
```

## Security Considerations

1. **IAM**: Use principle of least privilege
2. **Secrets**: Never commit secrets to version control
3. **Network**: Use private IP for database connections
4. **SSL**: Enforce SSL connections
5. **Updates**: Regularly update dependencies and base images

## Backup and Recovery

### Automated Backups

- Daily automated backups enabled
- 7-day retention policy
- Point-in-time recovery available

### Manual Backup

```bash
# Create on-demand backup
gcloud sql backups create \
    --instance=aequitas-db \
    --description="Manual backup $(date)"
```

### Disaster Recovery

1. Database can be restored from backups
2. Application deployments are versioned
3. Infrastructure can be recreated with Terraform