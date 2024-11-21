import unittest
from app.main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

    def test_404(self):
        response = self.app.get("/notfound")
        self.assertEqual(response.status_code, 404)

    def test_content_type(self):
        response = self.app.get("/")
        self.assertEqual(response.content_type, "application/json")
