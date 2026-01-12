import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# CONFIG
# -------------------------
SESSIONID = os.getenv("SESSIONID")
CSRFTOKEN = os.getenv("CSRFTOKEN")
USER_ID = os.getenv("USER_ID")

REQUEST_COUNT = 24
DELAY = 3
OUTPUT_FILE = "followers.csv"
# -------------------------

if not all([SESSIONID, CSRFTOKEN, USER_ID]):
    raise ValueError("Missing SESSIONID, CSRFTOKEN, or USER_ID in .env file")

headers = {
    "X-CSRFToken": CSRFTOKEN,
    "X-IG-App-ID": "936619743392459"
}

cookies = {
    "sessionid": SESSIONID,
    "csrftoken": CSRFTOKEN
}

url = f"https://www.instagram.com/api/v1/friendships/{USER_ID}/followers/"

def fetch_followers():
    followers = []
    max_id = None
    page = 1

    while True:
        params = {"count": REQUEST_COUNT}
        if max_id:
            params["max_id"] = max_id

        print(f"Fetching page {page} ...")
        response = requests.get(url, headers=headers, cookies=cookies, params=params)

        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            break

        data = response.json()
        users = data.get("users", [])

        if not users:
            print("No users found, stopping.")
            break

        for user in users:
            followers.append({
                "username": user.get("username"),
                "full_name": user.get("full_name"),
                "profile_pic_url": user.get("profile_pic_url"),
                "pk": user.get("pk"),
                "is_private": user.get("is_private"),
                "is_verified": user.get("is_verified")
            })

        if data.get("has_more"):
            max_id = data.get("next_max_id")
            page += 1
            time.sleep(DELAY)
        else:
            print("All followers fetched!")
            break

    return followers

def main():
    followers = fetch_followers()
    print(f"Total followers fetched: {len(followers)}")

    df = pd.DataFrame(followers)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved followers to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
