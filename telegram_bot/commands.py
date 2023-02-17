from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Update
)
from telegram.ext import (
    ContextTypes,
)
from telegram_bot.frames import FramesSection, get_partial_frame_section
from telegram_bot.utils import get_url_path_frame
from telegram_bot.constants import (
    EXIT,
    FIRST_FRAME,
    HOW_IT_WORK,
    LAST_FRAME,
    NO,
    PLAY,
    SELECTING_ACTION,
    SELECTING_FRAME,
    YES
)


# Telegram buttons
BUTTON_HOW_IT_WORK = InlineKeyboardButton(
    text="How it work", callback_data=str(HOW_IT_WORK)
)
BUTTON_PLAY = InlineKeyboardButton(text="Play", callback_data=str(PLAY))
BUTTON_EXIT = InlineKeyboardButton(text="Exit!", callback_data=str(EXIT))
BUTTON_YES = InlineKeyboardButton("Yes 😃!", callback_data=str(YES))
BUTTON_NO = InlineKeyboardButton("No 😐", callback_data=str(NO))


INILINE_KEYBOARD_FOR_PLAY = InlineKeyboardMarkup(
    [
        [BUTTON_YES, BUTTON_NO],
        [
            BUTTON_EXIT,
        ],
    ]
)
INILINE_KEYBOARD_FOR_START = InlineKeyboardMarkup(
    [
        [
            BUTTON_HOW_IT_WORK,
            BUTTON_PLAY,
        ],
        [
            BUTTON_EXIT,
        ],
    ]
)
INILINE_KEYBOARD_FOR_HOWITWORK = InlineKeyboardMarkup([[BUTTON_PLAY, BUTTON_EXIT]])


# Telegram commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Start robot to init interaction with the user"""
    await update.message.reply_text(
        text="Hi, I'm Dinex Bot and I'm here to help you to find an exact moment in a certain video",
        reply_markup=INILINE_KEYBOARD_FOR_START,
    )
    return SELECTING_ACTION


async def howitwork(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Send a message with the instructions for using the bot."""
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="1. Look at the image\n2. Read the question\n3. Respond as appropriate\n4. Repeat until you get the result",
        reply_markup=INILINE_KEYBOARD_FOR_HOWITWORK,
    )
    return SELECTING_ACTION


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Send a message with the frame, buttons and questions."""
    await update.callback_query.answer()
    
    response = update.callback_query.data

    # Start to find.
    if response == str(PLAY):
        context.user_data['frames_section'] = FramesSection(FIRST_FRAME, LAST_FRAME)
        url_path_frame = get_url_path_frame(context.user_data['frames_section'].get_median())
        await update.effective_message.reply_photo(
            photo=url_path_frame,
            caption="Did the rocket launch yet?",
            reply_markup=INILINE_KEYBOARD_FOR_PLAY,
        )
        return SELECTING_FRAME

    slice_toward_right = not response == str(YES)
    context.user_data['frames_section'] = get_partial_frame_section(context.user_data['frames_section'], slice_toward_right)

    # Already found it.
    if context.user_data['frames_section'].is_mid_equal_to_limit():
        await update.effective_message.reply_text(
            f"Found! Take-off = {context.user_data['frames_section'].get_median()}"
        )
        return EXIT

    # Keep finding.
    url_path_frame = get_url_path_frame(context.user_data['frames_section'].get_median())
    media = InputMediaPhoto(media=url_path_frame, caption="Did the rocket launch yet?")
    await update.callback_query.edit_message_media(
        media=media, reply_markup=INILINE_KEYBOARD_FOR_PLAY
    )
    return SELECTING_FRAME


async def exit_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """End Conversation by command."""
    await update.effective_message.reply_text("Okay, bye. Come back soon!")
    return EXIT
