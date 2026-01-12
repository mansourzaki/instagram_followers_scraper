# Instagram Followers Tool

A lightweight Python **template** for fetching **your own Instagram followers (username,fullname)** using an authenticated session.

This project is intended for **personal use, backups, or educational purposes**.

---

## ✨ Features

- Fetch followers from your **own Instagram account**
- Handles pagination using `max_id`
- Exports followers to CSV
- Minimal setup
- No credentials stored in the repository

---

## 📦 Requirements

- Python 3.7+
- An Instagram account
- Valid Instagram session cookies

---

## 🚀 Setup

### 1️⃣ Clone the repository

git clone https://github.com/mansourzaki/instagram_followers_scrapper.git
cd instagram_followers_scrapper

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ Create .env file

Copy the example file:

cp example.env .env

Edit `.env` and add your own values:

SESSIONID=your_instagram_sessionid
CSRFTOKEN=your_csrf_token
USER_ID=your_numeric_user_id

⚠️ Never commit or share your `.env` file.

### 4️⃣ Run the script

python insta_followers_app.py

The script will fetch all followers and save them to:
followers.csv

---

## ⚠️ Disclaimer & Legal Notice

This project is not affiliated with, endorsed by, or connected to Instagram or Meta.

This tool is intended for personal use only.

Do not use this tool to scrape other users’ private data.

Automated or abusive usage may violate Instagram’s Terms of Service.

Use this tool at your own risk.

You are responsible for complying with all applicable laws and platform policies.

---

## 🔐 Security Notes

- Never share your `SESSIONID` or `CSRFTOKEN`
- Keep `.env` files private
- Rotate your session credentials if you suspect exposure

---

## 🤝 Contributing

Pull requests are welcome for:

- Code improvements
- Better error handling
- Documentation enhancements