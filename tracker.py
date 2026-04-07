import requests
import json
import re
from datetime import datetime

USERNAME = "kristianstauding"
URL = f"https://www.tiktok.com/@{USERNAME}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
html = response.text

match = re.search(r'"followerCount":(\d+)', html)

followers = int(match.group(1)) if match else 0

data = {
    "followers": followers,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Updated:", followers)
