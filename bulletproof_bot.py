#!/usr/bin/env python3
import time
import urllib.request
import json
from datetime import datetime
import threading

TELEGRAM_TOKEN = '8565362564:AAGS86lij-0KayMPe2a9Pooxw85nj7XQlG8'
CHAT_ID = '52504489'

def send_telegram(msg):
    """Pure HTTP Telegram API - NO libraries"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': msg,
        'parse_mode': 'Markdown'
    }
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode(), headers={'Content-Type': 'application/json'})
        urllib.request.urlopen(req, timeout=10)
        print("✅ Message sent")
    except:
        pass

def startup():
    """First message"""
    msg = f"""✅ **BOT ALIVE** - 52504489
⏰ {datetime.now().strftime('%H:%M EET')}
🚀 Railway deployment OK
💰 Elite bets every 4hrs"""
    send_telegram(msg)

def elite_bet():
    """Elite bet alert"""
    msg = f"""🚨 **€20 ELITE BET**
⏰ {datetime.now().strftime('%H:%M EET')}

🥇 Greek Super League
⚔️ PAOK vs Volos NFC
📊 88% | Edge +17%

💰 **€20 @ 1.28**
💸 Payout: €25.60 (+28%)

🏦 Stoiximan | Max €20"""
    send_telegram(msg)

def main_loop():
    """Infinite loop - Railway stable"""
    startup()
    while True:
        elite_bet()
        time.sleep(14400)  # 4 hours

if __name__ == "__main__":
    print("🚀 MINIMAL BOT LIVE")
    main_loop()
