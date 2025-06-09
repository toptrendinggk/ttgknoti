import requests
import hashlib
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ✅ Your Telegram Bot Details
TELEGRAM_TOKEN = '7747463026:AAFmvpIh1dz78AOzxSkatZ68aU4RajGjdCM'
CHAT_ID = '608304987'

# ✅ All 21 RRB Website URLs
urls = {
    "https://www.rrbahmedabad.gov.in": "",
    "https://www.rrbajmer.gov.in": "",
    "https://www.rrbbangalore.gov.in": "",
    "https://www.rrbbhopal.gov.in": "",
    "https://www.rrbbhubaneswar.gov.in": "",
    "https://www.rrbbilaspur.gov.in": "",
    "https://www.rrbchandigarh.gov.in": "",
    "https://www.rrbchennai.gov.in": "",
    "https://www.rrbgkp.gov.in": "",
    "https://www.rrbguwahati.gov.in": "",
    "https://www.rrbjammu.nic.in": "",
    "https://www.rrbkolkata.gov.in": "",
    "https://www.rrbmalda.gov.in": "",
    "https://www.rrbmumbai.gov.in": "",
    "https://www.rrbmuzaffarpur.gov.in": "",
    "https://www.rrbpatna.gov.in": "",
    "https://www.rrbranchi.gov.in": "",
    "https://www.rrbsecunderabad.gov.in": "",
    "https://www.rrbsiliguri.gov.in": "",
    "https://www.rrbthiruvananthapuram.gov.in": "",
    "https://rrbald.gov.in": ""
}

def get_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

def send_telegram_message(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {'chat_id': CHAT_ID, 'text': message}
        requests.post(url, data=data)
    except Exception as e:
        print(f"Telegram error: {e}")

def check_websites():
    for site in urls:
        try:
            res = requests.get(site, timeout=15, verify=False)
            h = get_hash(res.text)
            if urls[site] and urls[site] != h:
                send_telegram_message(f"🔄 Change detected at: {site}")
            urls[site] = h
        except Exception as e:
            send_telegram_message(f"⚠️ Error checking {site}: {e}")

if __name__ == "__main__":
    while True:
        check_websites()
        time.sleep(60)
