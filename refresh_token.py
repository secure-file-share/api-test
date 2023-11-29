import unittest
import requests


class TestAuthTokenRefreshEndpoint(unittest.TestCase):

    def setUp(self):
        # Replace '{{host}}' with the actual base URL of your API
        self.base_url = "https://securefileshare.pythonanywhere.com"
        self.refresh_endpoint = "/api/auth/token/refresh/"

    def test_refresh_token_successful(self):
        # Replace '{{refresh}}' with a valid refresh token for testing
        payload = {
            "refresh": "", "access": ""
        }

        # Make a POST request to the refresh token endpoint
        response = requests.post(
            self.base_url + self.refresh_endpoint, json=payload)

        # Assert that the response status code is 200 (or the expected status code)
        self.assertEqual(response.status_code, 200)

        # You can add more assertions based on your API response structure
        # For example, checking if the response contains a new access token

        # Example assertion for a JSON response containing a 'access_token' key
        response_json = response.json()
        self.assertIn("access", response_json)

    def test_refresh_token_failed(self):
        # Test for unsuccessful token refresh (e.g., expired refresh token)
        payload = {
            "refresh": "expired_refresh_token"
        }

        response = requests.post(
            self.base_url + self.refresh_endpoint, json=payload)

        # Assert that the response status code is the expected code for failed refresh
        self.assertEqual(response.status_code, 401)

        # You can add more assertions based on your API response structure


if __name__ == '__main__':
    unittest.main()
