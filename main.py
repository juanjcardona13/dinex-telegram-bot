#!/usr/bin/env python
import os
from telegram_bot.main import TelegramBot


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = TelegramBot(TELEGRAM_TOKEN)

if __name__ == "__main__":
    bot.run()
