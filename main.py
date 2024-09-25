import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    print("Missing ENV", flush=True)

BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPoll'
parameters = {
    "chat_id" : CHAT_ID,
    "question" : f"Are you in office today? {datetime.today().strftime('%d/%m/%y')}",
    "options" : json.dumps(["CBP", "No"]),
    "is_anonymous" : False
}

def main():
    resp = requests.get(BASE_URL, data=parameters)
    print(resp.text, flush=True)


if __name__ == "__main__":
    main()