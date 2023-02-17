
from urllib.parse import quote, urljoin
from telegram_bot.constants import API_BASE, VIDEO_NAME
<<<<<<< HEAD
=======
from telegram_bot.frames import FramesSection
>>>>>>> 1e11dbe54641d5a296873714a70e4ad3750716c1

def get_url_path_frame(frame: int) -> str:
    """
    Buld path for frame.

    Args:
        frame (:obj:`int`): The ``frame`` to buld url path for get frame

    Returns:
        :obj:`str`: The url path
    """
    return urljoin(API_BASE, f'video/{quote(VIDEO_NAME)}/frame/{quote(f"{frame}")}/')
