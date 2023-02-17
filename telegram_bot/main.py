from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
)
from telegram_bot.constants import (
    EXIT,
    HOW_IT_WORK,
    NO,
    PLAY,
    SELECTING_ACTION,
    SELECTING_FRAME,
    YES,
)
from telegram_bot.commands import exit_command, howitwork, play, start

class TelegramBot:
    """
    Utility class to run telegram bot
    """

    def __init__(self, telegram_token) -> None:
        self.app = Application.builder().token(telegram_token).build()

    def run(self):
        """Run the bot."""
        # Set up Find-Frame level ConversationHandler
        handle_frame_selection = ConversationHandler(
            entry_points=[CallbackQueryHandler(play, pattern=f"^{str(PLAY)}$")],
            states={
                SELECTING_FRAME: [
                    CallbackQueryHandler(play, pattern=f"^{str(YES)}$"),
                    CallbackQueryHandler(play, pattern=f"^{str(NO)}$"),
                    CallbackQueryHandler(exit_command, pattern=f"^{str(EXIT)}$"),
                ]
            },
            fallbacks=[
                CommandHandler("exit", exit_command),
            ],
            map_to_parent={
                EXIT: EXIT,
            },
        )

        # Set up top level ConversationHandler (Selecting action)
        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start)],
            states={
                SELECTING_ACTION: [
                    handle_frame_selection,
                    CallbackQueryHandler(howitwork, pattern=f"^{str(HOW_IT_WORK)}$"),
                    CallbackQueryHandler(play, pattern=f"^{str(PLAY)}$"),
                    CallbackQueryHandler(exit_command, pattern=f"^{str(EXIT)}$"),
                ],
            },
            fallbacks=[CommandHandler("exit", exit_command)],
            per_chat=True,
            per_user=True
        )

        self.app.add_handler(conversation_handler)

        # Run the bot
        self.app.run_polling()
