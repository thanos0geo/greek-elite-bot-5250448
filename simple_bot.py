import schedule
import time
import telegram
import asyncio
import random
from datetime import datetime

# YOUR LIVE KEYS
TELEGRAM_TOKEN = '8565362564:AAGS86lij-0KayMPe2a9Pooxw85nj7XQlG8'
CHAT_ID = '52504489'

bot = telegram.Bot(token=TELEGRAM_TOKEN)

async def send_test_message():
    """Test message - confirms bot works"""
    await bot.send_message(
        chat_id=CHAT_ID, 
        text=f"🚀 **BOT LIVE!** ID:52504489
⏰ {datetime.now().strftime('%H:%M EET')}
✅ Railway deployment SUCCESSFUL",
        parse_mode='Markdown'
    )

async def send_elite_bet():
    """Simple elite bet example"""
    bets = [
        {"team": "PAOK vs Volos", "stake": "€20", "odds": "1.28", "prob": "85%"},
        {"team": "Bayern vs Bochum", "stake": "€18", "odds": "1.22", "prob": "89%"} 
    ]
    
    msg = f"🚨 **ELITE BET ALERT** - 75% Accuracy
⏰ {datetime.now().strftime('%H:%M EET')}

"
    
    for bet in random.sample(bets, min(1, len(bets))):
        msg += f"🥇 **{bet['team']}**
"
        msg += f"💰 **{bet['stake']} @ {bet['odds']}** ({bet['prob']})
"
        msg += f"💸 Payout: €{float(bet['stake'][1:]) * float(bet['odds']):.0f}

"
    
    msg += f"🏦 Bankroll: €100 | *Stoiximan Ready* | Max €20"
    await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode='Markdown')

async def main_loop():
    """Send alerts every 2 hours"""
    await send_test_message()
    print("✅ TEST MESSAGE SENT - Bot working!")
    
    # Schedule elite bets
    schedule.every(2).hours.do(lambda: asyncio.run(send_elite_bet()))
    schedule.every().day.at("08:00").do(lambda: asyncio.run(send_elite_bet()))
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    print("🚀 PRODUCTION BOT STARTING...")
    asyncio.run(main_loop())