import requests
import json
import re
from datetime import datetime

USERNAME = "kristianstauding"
URL = f"https://www.tiktok.com/@{USERNAME}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

followers = 0

try:
    response = requests.get(URL, headers=headers, timeout=10)
    html = response.text

    match = re.search(r'"followerCount":(\d+)', html)

    if match:
        followers = int(match.group(1))

except Exception as e:
    print("FEJL:", e)

data = {
    "followers": followers,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Updated:", followers)
