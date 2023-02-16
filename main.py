#!/usr/bin/env python
from telegram_bot.constants import TELEGRAM_TOKEN
from telegram_bot.main import TelegramBot


bot = TelegramBot(TELEGRAM_TOKEN)

if __name__ == "__main__":
    bot.run()
