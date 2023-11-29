import unittest
import requests


class TestAuthTokenLoginEndpoint(unittest.TestCase):

    def setUp(self):
        # Replace '{{host}}' with the actual base URL of your API
        self.base_url = "https://securefileshare.pythonanywhere.com"
        self.login_endpoint = "/api/auth/token/login/"

    def test_login_successful(self):
        # Replace with valid credentials for testing
        payload = {
            "username": "your_username",
            "password": "your_password"
        }

        # Make a POST request to the login endpoint
        response = requests.post(
            self.base_url + self.login_endpoint, json=payload)

        # print(response.text)
        # Assert that the response status code is 200 (or the expected status code)
        self.assertEqual(response.status_code, 200)

        # You can add more assertions based on your API response structure
        # For example, checking if the response contains a token

        # Example assertion for a JSON response containing a 'token' key
        response_json = response.json()
        self.assertIn("access", response_json)

    def test_login_failed(self):
        # Test for unsuccessful login (e.g., incorrect credentials)
        payload = {
            "username": "invalid_username",
            "password": "invalid_password"
        }

        response = requests.post(
            self.base_url + self.login_endpoint, json=payload)

        # Assert that the response status code is the expected code for failed login
        self.assertEqual(response.status_code, 401)

        # You can add more assertions based on your API response structure


if __name__ == '__main__':
    unittest.main()
