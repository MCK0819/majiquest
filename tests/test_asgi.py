from unittest.mock import patch

from django.test import TestCase


class AsgiTest(TestCase):
    def test_asgi_application(self):
        with patch("django.core.asgi.get_asgi_application"):
            response = self.client.get("/api/schema/swagger-ui/")
            self.assertEqual(response.status_code, 200)
