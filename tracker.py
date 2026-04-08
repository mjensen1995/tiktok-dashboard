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

while True:
    try:
        # hent data fra TikTok
        response = requests.get(URL, headers=headers)
        html = response.text

        match = re.search(r'"followerCount":(\d+)', html)
        followers = int(match.group(1)) if match else 0

        data = {
            "followers": followers,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # gem lokalt
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

        print("Opdateret:", followers)

        # ===== UPLOAD TIL SIMPLY =====
        ftp = FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)

        # VIGTIGT: ret sti hvis du bruger /dashboard/
        ftp.cwd("public_html/dashboard")

        with open("data.json", "rb") as f:
            ftp.storbinary("STOR data.json", f)

        ftp.quit()

        print("Uploadet til hjemmeside")

    except Exception as e:
        print("Fejl:", e)

    time.sleep(60)
