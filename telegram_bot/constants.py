import os
from telegram.ext import (ConversationHandler)

<<<<<<< HEAD
=======
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TOKEN")
>>>>>>> 1e11dbe54641d5a296873714a70e4ad3750716c1
API_BASE = os.getenv("API_BASE", "https://framex-dev.wadrid.net/api/")
VIDEO_NAME = os.getenv(
    "VIDEO_NAME", "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
)

FIRST_FRAME: int = 0
LAST_FRAME: int = 61695


# State definitions for conversation
SELECTING_ACTION, SELECTING_FRAME = map(chr, range(2))

# Actions definitions for conversation
PLAY, HOW_IT_WORK, YES, NO = map(chr, range(2, 6))

# Shortcut for ConversationHandler.END
EXIT = ConversationHandler.END
