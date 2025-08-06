# Aequitas
Social Media for Parents with disabled children

## Table of Contents
- [Overview](#overview)
- [Local Development](#local-development)
- [Environment Configuration](#environment-configuration)
- [Docker Usage](#docker-usage)

## Overview

Aequitas is a Django-based social media platform designed specifically for parents with disabled children. The application provides a supportive community platform with modern features and is optimized for local development.

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
docker compose up --build
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
docker compose up --build

# Production
cp .env.sample .env
# Edit .env with production values
docker compose up -d --build
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
- **Security optimized**: Production security settings when DEBUG=False

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally using the development environment
5. Submit a pull request

## License

This project is licensed under the terms specified in the LICENSE file.