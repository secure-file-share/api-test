import unittest
import requests


class TestFileUploadAPI(unittest.TestCase):
    base_url = " https://securefileshare.pythonanywhere.com/api/fileshare/fileshare/"
    login_url = " https://securefileshare.pythonanywhere.com/api/auth/token/login/"

    def setUp(self):
        # Perform login and get the access token
        self.access_token = self.get_access_token()

        # Use the obtained access token for authorization
        self.headers = {'Authorization': f'Bearer {self.access_token}',
                        # 'Content-Type': 'multipart/form-data'
                        }

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

    def test_file_upload_api(self):
        # Path to the file you want to upload
        file_path = "./testfile.txt"

        # Username of the user to share the file with
        shared_to_username = "username"

        file_to_share = open(file_path, 'rb')

        # Prepare form data
        form_data = {
            'shared_to': shared_to_username,
        }

        # Assuming the field name is 'file'
        form_data_files = [
            ('file', ('testfile.txt', file_to_share, 'application/octet-stream'))]

        response = requests.post(
            self.base_url, headers=self.headers, data=form_data, files=form_data_files)

        file_to_share.close()

        # Assuming a successful response has a status code of 201
        self.assertEqual(response.status_code, 201,
                         f"Expected status code 201, but got {response.status_code}")

        # You may add more specific assertions based on your API response structure
        upload_response = response.json()
        self.assertIsNotNone(upload_response)
        # Add more assertions as needed


if __name__ == '__main__':
    unittest.main()
