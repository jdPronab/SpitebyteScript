import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

API_URL = "https://spacebyte.in/api/v1"
API_TOKEN = os.getenv("API_TOKEN")

headers = {"Authorization": f"Bearer {API_TOKEN}"}
payload = {"file" : "VIDEOS/500m6.mp4"}
upload_url =  API_URL+"/uploads"
# res = requests.post(upload_url, headers=headers, data=payload)
res = requests.get(f"{API_URL}/drive/file-entries", headers=headers)
print(res.content)
