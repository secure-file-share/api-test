import unittest
import requests


class TestDeleteFileAPI(unittest.TestCase):
    base_url = " https://securefileshare.pythonanywhere.com/api/fileshare/fileshare/"
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

    def test_delete_file_api(self):
        # Replace 'file_share_link_id' with the actual file share link ID
        file_share_link_id = "file_share_link_id"

        url = f"{self.base_url}{file_share_link_id}/"
        response = requests.delete(url, headers=self.headers)

        # Assuming a successful response has a status code of 200
        self.assertEqual(response.status_code, 200,
                         f"Expected status code 200, but got {response.status_code}")

        # You may add more specific assertions based on your API response or behavior
        # For example, check if the file is actually deleted or if a proper response is returned
        # Example: self.assertEqual(response.json(), {'message': 'File deleted successfully'})


if __name__ == '__main__':
    unittest.main()
