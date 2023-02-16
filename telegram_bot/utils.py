
from urllib.parse import quote, urljoin
from telegram_bot.constants import API_BASE, VIDEO_NAME
from telegram_bot.frames import FramesSection

def get_url_path_frame(frame: int) -> str:
    """
    Buld path for frame.

    Args:
        frame (:obj:`int`): The ``frame`` to buld url path for get frame

    Returns:
        :obj:`str`: The url path
    """
    return urljoin(API_BASE, f'video/{quote(VIDEO_NAME)}/frame/{quote(f"{frame}")}/')
