import requests
import json
import re
import os
import time
from datetime import datetime
from ftplib import FTP

# ===== DINE INFO =====
USERNAME = "kristianstauding"

FTP_HOST = "ftp.simply.com"
FTP_USER = "tiktok-follower.dk"
FTP_PASS = "nb9hxpyF4k56D2a3zEwd"

URL = f"https://www.tiktok.com/@{USERNAME}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# sørger for korrekt mappe
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("🔥 Tracker startet – opdaterer hvert 60 sek")

while True:
    try:
        print("Henter data...")

        response = requests.get(URL, headers=headers)
        html = response.text

        match = re.search(r'"followerCount":(\d+)', html)
        followers = int(match.group(1)) if match else 0

        data = {
            "followers": followers,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # GEM LOKALT
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

        print("✔ Opdateret:", followers)

        # ===== FTP UPLOAD =====
        print("Uploader til server...")

        ftp = FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)

        # 🔴 PRØV DENNE FØRST
        ftp.cwd("public_html/dashboard")

        with open("data.json", "rb") as f:
            ftp.storbinary("STOR data.json", f)

        ftp.quit()

        print("🌍 Upload OK")

    except Exception as e:
        print("❌ FEJL:", e)

    time.sleep(60)