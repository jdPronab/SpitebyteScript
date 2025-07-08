import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

class SpaceByte:
    def __init__(self, token):
        self.url = "https://spacebyte.in/api/v1"
        self.headers = {
            'accept': 'application/json',
            "Authorization": f"Bearer {token}"
            }

    def upload_video(self, file_path):
        upload_url =  f"{self.url}/uploads"
        files = {
            'file': (file_path, open(file_path, 'rb'), 'video/mp4'),
            'parentId': (None, 'null'),
            'relativePath': (None, ''),
        }
        res = requests.post(upload_url, headers=self.headers, files=files)
        return res

    def get_shareable_link(self, id):
        url = f"{self.url}/file-entries/{id}/shareable-link"
        res = requests.get(url, headers=self.headers)
        print(json.loads(res.text))
        data = json.loads(res.text)['data']
        file_name = data['link'][0]['entry']['file_name']
        link = f"https://spacebyte.in/drive/s/{file_name}"
        return link

    def file_entries(self):
        url =  f"{self.url}/drive/file-entries"
        res = requests.get(url, headers=self.headers)
        return res



if __name__ == "__main__":
    sb = SpaceByte(API_TOKEN)
    

