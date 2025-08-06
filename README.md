# Aequitas
Social Media for Parents with disabled children

## Table of Contents
- [Overview](#overview)
- [Local Development](#local-development)
- [Cloud Deployment](#cloud-deployment)
  - [Google Cloud Platform](#google-cloud-platform)
  - [DigitalOcean](#digitalocean)
- [Environment Configuration](#environment-configuration)
- [Docker Usage](#docker-usage)

## Overview

Aequitas is a Django-based social media platform designed specifically for parents with disabled children. The application provides a supportive community platform with modern features and cloud-ready deployment.

## Local Development

### Prerequisites
- Python 3.12+
- Docker and Docker Compose (optional but recommended)

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/chaene82/aequitas.git
cd aequitas
```

2. Set up environment variables:
```bash
cp .env.development.sample .env
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations and start development server:
```bash
cd app
python manage.py migrate
python manage.py runserver
```

### Using Docker for Development

1. Copy environment file:
```bash
cp .env.development.sample .env
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

## Cloud Deployment

Aequitas supports deployment on multiple cloud platforms with different levels of complexity and features.

### Google Cloud Platform

For a fully managed, scalable deployment with Cloud SQL PostgreSQL database, use Google Cloud Platform.

#### Quick Google Cloud Deployment

```bash
# Clone the repository
git clone https://github.com/chaene82/aequitas.git
cd aequitas

# Run the automated deployment script
./deploy-gcloud.sh YOUR_GCP_PROJECT_ID us-central1
```

#### Manual Google Cloud Deployment

1. **Set up infrastructure with Terraform**:
```bash
cd terraform
terraform init
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your project details
terraform apply
```

2. **Build and deploy application**:
```bash
gcloud builds submit --config cloudbuild.yaml
```

For detailed instructions, see [Google Cloud Deployment Guide](docs/gcloud-deployment.md).

#### Google Cloud Features
- **Cloud Run**: Serverless container hosting with automatic scaling
- **Cloud SQL**: Managed PostgreSQL database with backups
- **Secret Manager**: Secure configuration management
- **Cloud Build**: Automated CI/CD pipeline
- **Private networking**: VPC with private database access

### DigitalOcean

This application is optimized for cloud deployment on DigitalOcean using Docker, PostgreSQL, and efficient static file serving.

#### Option 1: DigitalOcean App Platform (Recommended)

#### Prerequisites
- DigitalOcean account
- GitHub repository connected to DigitalOcean

#### Deployment Steps

1. **Prepare Environment Variables**
   
   Create production environment variables based on `.env.sample`:
   ```
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=aequitas_prod
   DB_USER=aequitas_user
   DB_PASS=your_secure_password_here
   SECRET_KEY=your_very_secure_secret_key_here_change_this_in_production
   DEBUG=0
   ENV=PROD
   ALLOWED_HOSTS=your-domain.com,www.your-domain.com
   PORT=8000
   ```

2. **Create App on DigitalOcean App Platform**
   
   - Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)
   - Click "Create App"
   - Connect your GitHub repository
   - Configure the following:

3. **App Configuration**
   
   **Web Service:**
   - Source: Your GitHub repository
   - Branch: main
   - Auto Deploy: Yes
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `gunicorn --pythonpath app app.wsgi:application --bind 0.0.0.0:$PORT`
   
   **Database:**
   - Add a PostgreSQL database component
   - Plan: Basic ($7/month minimum)
   - Name: `aequitas-db`

4. **Environment Variables**
   
   In the App Settings, add all environment variables from step 1.
   DigitalOcean will automatically provide database connection details.

5. **Deploy**
   
   Click "Create Resources" to deploy your application.

#### Option 2: DigitalOcean Droplets with Docker

#### Prerequisites
- DigitalOcean Droplet (Ubuntu 22.04 recommended)
- Docker and Docker Compose installed on droplet

#### Deployment Steps

1. **Set up Droplet**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install Docker Compose
sudo apt install docker-compose-plugin -y
```

2. **Deploy Application**
```bash
# Clone repository
git clone https://github.com/chaene82/aequitas.git
cd aequitas

# Configure environment
cp .env.sample .env
# Edit .env with your production values
nano .env

# Deploy with Docker Compose
docker compose up -d --build
```

3. **Set up Reverse Proxy (Optional)**
   
   Configure Nginx or use the included proxy service for SSL and domain management.

#### Option 3: Using Procfile (Heroku-compatible platforms)

The application includes a `Procfile` for deployment on Heroku-compatible platforms:

```
web: gunicorn --pythonpath app app.wsgi:application --bind 0.0.0.0:$PORT
release: python app/manage.py migrate
```

## Environment Configuration

### Development Environment

Create `.env` based on `.env.development.sample`:
```env
# Development uses SQLite by default
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
SECRET_KEY=dev-secret-key-change-in-production
DEBUG=1
ENV=DEV
ALLOWED_HOSTS=127.0.0.1,localhost
PORT=8000
```

### Production Environment

Create `.env` based on `.env.sample`:
```env
# Production uses PostgreSQL
DB_ENGINE=django.db.backends.postgresql
DB_NAME=aequitas_prod
DB_USER=aequitas_user
DB_PASS=your_secure_password_here
DB_HOST=db
DB_PORT=5432
SECRET_KEY=your_very_secure_secret_key_here
DEBUG=0
ENV=PROD
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
PORT=8000
```

## Docker Usage

### Building the Application

```bash
docker build -t aequitas .
```

### Running with Docker Compose

```bash
# Development
cp .env.development.sample .env
docker-compose up --build

# Production
cp .env.sample .env
# Edit .env with production values
docker-compose up -d --build
```

### Services Included

- **app**: Django application server
- **db**: PostgreSQL database
- **proxy**: Nginx reverse proxy for static files

## Key Features

- **Environment-based configuration**: Supports both development and production setups
- **Static file optimization**: WhiteNoise for efficient static file serving
- **Database flexibility**: SQLite for development, PostgreSQL for production
- **Container ready**: Docker and Docker Compose configuration
- **Cloud platform ready**: Procfile and environment variable support
- **Security optimized**: Production security settings when DEBUG=False

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally using the development environment
5. Submit a pull request

## License

This project is licensed under the terms specified in the LICENSE file.
