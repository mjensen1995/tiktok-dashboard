import requests
import json
import re
from datetime import datetime

USERNAME = "kristianstauding"
URL = f"https://www.tiktok.com/@{USERNAME}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(URL, headers=headers)
html = response.text

# Hent præcist follower-tal
match = re.search(r'"followerCount":(\d+)', html)

if match:
    followers = int(match.group(1))
else:
    followers = 0

data = {
    "followers": followers,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M")
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Opdateret:", followers)
