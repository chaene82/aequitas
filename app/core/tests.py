from django.test import TestCase, Client
from django.urls import reverse


class HealthCheckTests(TestCase):
    """Tests for the health check endpoint"""
    
    def setUp(self):
        self.client = Client()
    
    def test_health_check_get_allowed(self):
        """Test that GET requests are allowed on health endpoint"""
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'healthy', 'service': 'aequitas'})
    
    def test_health_check_post_not_allowed(self):
        """Test that POST requests are not allowed on health endpoint"""
        response = self.client.post('/health/', {})
        self.assertEqual(response.status_code, 405)  # Method Not Allowed
    
    def test_health_check_put_not_allowed(self):
        """Test that PUT requests are not allowed on health endpoint"""
        response = self.client.put('/health/', {})
        self.assertEqual(response.status_code, 405)  # Method Not Allowed
