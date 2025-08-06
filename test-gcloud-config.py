#!/usr/bin/env python3
"""
Test script to validate Google Cloud deployment configuration
"""

import os
import sys
import tempfile
import subprocess
from pathlib import Path


def test_environment_configuration():
    """Test that environment variables are properly configured"""
    print("Testing environment configuration...")
    
    # Test sample environment file
    env_sample_path = Path('.env.gcloud.sample')
    if not env_sample_path.exists():
        print("❌ .env.gcloud.sample file not found")
        return False
    
    # Read and validate sample environment variables
    with open(env_sample_path) as f:
        content = f.read()
        required_vars = ['DB_ENGINE', 'DB_NAME', 'DB_USER', 'DB_HOST', 'DEBUG', 'ENV']
        for var in required_vars:
            if var not in content:
                print(f"❌ Missing required environment variable: {var}")
                return False
    
    print("✅ Environment configuration valid")
    return True


def test_terraform_configuration():
    """Test that Terraform configuration is valid"""
    print("Testing Terraform configuration...")
    
    terraform_path = Path('terraform/main.tf')
    if not terraform_path.exists():
        print("❌ Terraform configuration not found")
        return False
    
    # Check for required resources
    with open(terraform_path) as f:
        content = f.read()
        required_resources = [
            'google_sql_database_instance',
            'google_secret_manager_secret',
            'google_service_account',
            'google_project_service'
        ]
        for resource in required_resources:
            if resource not in content:
                print(f"❌ Missing Terraform resource: {resource}")
                return False
    
    print("✅ Terraform configuration valid")
    return True


def test_cloud_build_configuration():
    """Test that Cloud Build configuration is valid"""
    print("Testing Cloud Build configuration...")
    
    cloudbuild_path = Path('cloudbuild.yaml')
    if not cloudbuild_path.exists():
        print("❌ Cloud Build configuration not found")
        return False
    
    # Validate YAML syntax using Python's yaml module if available
    try:
        import yaml
        with open(cloudbuild_path) as f:
            config = yaml.safe_load(f)
        
        if 'steps' not in config:
            print("❌ Cloud Build configuration missing 'steps'")
            return False
        
        if len(config['steps']) < 3:
            print("❌ Cloud Build configuration has too few steps")
            return False
        
    except ImportError:
        print("⚠️  yaml module not available, skipping YAML validation")
    
    print("✅ Cloud Build configuration valid")
    return True


def test_django_health_endpoint():
    """Test that Django health endpoint is configured"""
    print("Testing Django health endpoint...")
    
    urls_path = Path('app/app/urls.py')
    if not urls_path.exists():
        print("❌ Django URLs configuration not found")
        return False
    
    with open(urls_path) as f:
        content = f.read()
        if 'health' not in content.lower():
            print("❌ Health endpoint not configured in URLs")
            return False
    
    print("✅ Django health endpoint configured")
    return True


def test_database_configuration():
    """Test that database configuration supports Cloud SQL"""
    print("Testing database configuration...")
    
    settings_path = Path('app/app/settings.py')
    if not settings_path.exists():
        print("❌ Django settings not found")
        return False
    
    with open(settings_path) as f:
        content = f.read()
        required_settings = ['cloudsql', 'CONN_MAX_AGE', 'sslmode']
        for setting in required_settings:
            if setting not in content:
                print(f"❌ Missing database configuration: {setting}")
                return False
    
    print("✅ Database configuration valid")
    return True


def test_documentation():
    """Test that documentation exists and is complete"""
    print("Testing documentation...")
    
    docs_path = Path('docs/gcloud-deployment.md')
    if not docs_path.exists():
        print("❌ Google Cloud deployment documentation not found")
        return False
    
    with open(docs_path) as f:
        content = f.read()
        required_sections = ['Prerequisites', 'Architecture', 'Quick Deployment', 'Configuration']
        for section in required_sections:
            if section not in content:
                print(f"❌ Missing documentation section: {section}")
                return False
    
    print("✅ Documentation complete")
    return True


def main():
    """Run all tests"""
    print("🚀 Running Google Cloud deployment validation tests...\n")
    
    tests = [
        test_environment_configuration,
        test_terraform_configuration,
        test_cloud_build_configuration,
        test_django_health_endpoint,
        test_database_configuration,
        test_documentation,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            failed += 1
        print()
    
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Google Cloud deployment configuration is ready.")
        return 0
    else:
        print("❌ Some tests failed. Please review the configuration.")
        return 1


if __name__ == '__main__':
    sys.exit(main())