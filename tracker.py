import requests
import json
import re
from datetime import datetime

USERNAME = "kristianstauding"
URL = f"https://www.tiktok.com/@{USERNAME}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

followers = 0  # fallback

try:
    print("Henter TikTok data...")

    response = requests.get(URL, headers=headers, timeout=10)

    if response.status_code != 200:
        print("Fejl status:", response.status_code)
    else:
        html = response.text

        match = re.search(r'"followerCount":(\d+)', html)

        if match:
            followers = int(match.group(1))
        else:
            print("Kunne ikke finde followerCount")

except Exception as e:
    print("FEJL:", e)

# ALDRIG crash – altid output
data = {
    "followers": followers,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Updated:", followers)
