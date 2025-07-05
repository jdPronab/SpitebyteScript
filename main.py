import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

# res = requests.post(upload_url, headers=headers, data=payload)
# res = requests.get(f"{API_URL}/drive/file-entries", headers=headers)
# data = json.loads(res.text)['data'][0]
# file_id = data['id']
# print(file_id)

class SpaceByte:
    def __init__(self, token):
        self.url = "https://spacebyte.in/api/v1"
        self.headers = {"Authorization": f"Bearer {token}",
                        'Content-Type' : 'multipart/form-data'}

    def upload_video(self, file_path):
        upload_url =  f"{self.url}/uploads"
        files = {'file': open(file_path, 'rb')}
        res = requests.post(upload_url, headers=self.headers, files=files)
        return res

    def get_shareable_link(self, id):
        pass


if __name__ == "__main__":
    sb = SpaceByte(API_TOKEN)
    res = sb.upload_video("/home/jyt/Pro/SpaceByteAPITest/VIDEOS/500m6.mp4")
    print(res)

