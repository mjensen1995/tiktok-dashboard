import json
from datetime import datetime

followers = 12345  # fallback

try:
    import requests
    import re

    USERNAME = "kristianstauding"
    URL = f"https://www.tiktok.com/@{USERNAME}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers, timeout=10)

    if response.status_code == 200:
        html = response.text
        match = re.search(r'"followerCount":(\d+)', html)

        if match:
            followers = int(match.group(1))

except Exception as e:
    print("Fejl men fortsætter:", e)

# ALDRIG STOP
data = {
    "followers": followers,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Updated:", followers)
