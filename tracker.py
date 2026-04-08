import json
from datetime import datetime

# TEST DATA (vi starter simpelt)
followers = 12345

data = {
    "followers": followers,
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Updated:", followers)
