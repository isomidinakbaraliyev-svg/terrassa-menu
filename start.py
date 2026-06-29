import threading
import os
from app import app
from bot import app as telegram_bot

def run_bot():
    telegram_bot.run_polling()

threading.Thread(target=run_bot).start()

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
