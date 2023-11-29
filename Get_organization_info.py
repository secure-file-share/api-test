import unittest
import requests


class TestGetOrganizationInfoAPI(unittest.TestCase):
    base_url = " https://securefileshare.pythonanywhere.com/api/organization/organization/"
    login_url = " https://securefileshare.pythonanywhere.com/api/auth/token/login/"

    def setUp(self):
        # Perform login and get the access token
        self.access_token = self.get_access_token()

        # Use the obtained access token for authorization
        self.headers = {'Authorization': f'Bearer {self.access_token}'}

    def get_access_token(self):
        # Replace 'your_username' and 'your_password' with actual credentials
        login_data = {
            'username': 'your_username',
            'password': 'your_password',
        }

        login_response = requests.post(self.login_url, json=login_data)

        # Assuming a successful login response has a status code of 200
        self.assertEqual(login_response.status_code, 200)

        # Extract and return the access token from the login response
        return login_response.json()['access']

    def test_get_organization_info_api(self):
        response = requests.get(self.base_url, headers=self.headers)

        # Assuming a successful response has a status code of 200
        self.assertEqual(response.status_code, 200,
                         f"Expected status code 200, but got {response.status_code}")

        # You may add more specific assertions based on your API response structure
        organization_info = response.json()
        self.assertIsNotNone(organization_info)
        # Add more assertions as needed


if __name__ == '__main__':
    unittest.main()
