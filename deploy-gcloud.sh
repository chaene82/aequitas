#!/bin/bash

# Aequitas Google Cloud Deployment Script
# This script deploys the Aequitas application to Google Cloud Platform

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
PROJECT_ID=${1:-""}
REGION=${2:-"us-central1"}
DB_INSTANCE_NAME="aequitas-db"
SERVICE_NAME="aequitas-app"

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if PROJECT_ID is provided
if [ -z "$PROJECT_ID" ]; then
    print_error "Usage: $0 <PROJECT_ID> [REGION]"
    print_error "Example: $0 my-gcp-project us-central1"
    exit 1
fi

print_status "Starting deployment of Aequitas to Google Cloud"
print_status "Project ID: $PROJECT_ID"
print_status "Region: $REGION"

# Check if gcloud is installed and authenticated
if ! command -v gcloud &> /dev/null; then
    print_error "gcloud CLI is not installed. Please install it first."
    exit 1
fi

# Set the project
print_status "Setting GCP project to $PROJECT_ID"
gcloud config set project $PROJECT_ID

# Check if terraform is available for infrastructure setup
if command -v terraform &> /dev/null; then
    print_status "Terraform detected. Setting up infrastructure..."
    cd terraform
    
    # Initialize Terraform if not already done
    if [ ! -d ".terraform" ]; then
        print_status "Initializing Terraform..."
        terraform init
    fi
    
    # Create terraform.tfvars if it doesn't exist
    if [ ! -f "terraform.tfvars" ]; then
        print_warning "terraform.tfvars not found. Creating from example..."
        cp terraform.tfvars.example terraform.tfvars
        sed -i "s/your-gcp-project-id/$PROJECT_ID/g" terraform.tfvars
        sed -i "s/us-central1/$REGION/g" terraform.tfvars
        print_warning "Please review and update terraform.tfvars before proceeding"
        read -p "Press Enter to continue or Ctrl+C to abort..."
    fi
    
    # Plan and apply infrastructure
    print_status "Planning Terraform deployment..."
    terraform plan
    
    print_status "Applying Terraform configuration..."
    terraform apply -auto-approve
    
    cd ..
else
    print_warning "Terraform not found. Please set up infrastructure manually or install Terraform."
fi

# Build and deploy using Cloud Build
print_status "Building and deploying application..."

# Replace PROJECT_ID placeholder in cloud-run-service.yaml
sed "s/PROJECT_ID/$PROJECT_ID/g" cloud-run-service.yaml > cloud-run-service-deploy.yaml

# Submit build to Cloud Build
print_status "Submitting build to Google Cloud Build..."
gcloud builds submit \
    --config cloudbuild.yaml \
    --substitutions=_REGION=$REGION,_PROJECT_ID=$PROJECT_ID \
    .

# Wait for deployment to complete
print_status "Waiting for deployment to complete..."
sleep 30

# Get the service URL
SERVICE_URL=$(gcloud run services describe $SERVICE_NAME --region=$REGION --format="value(status.url)")

print_status "Deployment completed successfully!"
print_status "Service URL: $SERVICE_URL"
print_status "Health check: $SERVICE_URL/health/"

# Clean up temporary files
rm -f cloud-run-service-deploy.yaml

print_status "Aequitas has been successfully deployed to Google Cloud!"
print_status "Next steps:"
echo "1. Visit the admin panel: $SERVICE_URL/admin/"
echo "2. Check application health: $SERVICE_URL/health/"
echo "3. Monitor logs: gcloud logs tail --service=$SERVICE_NAME"