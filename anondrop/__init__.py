from .main import upload, delete, UploadOutput
from .config import CLIENT_ID


def setClientID(client_id: str):
    from . import config

    config.CLIENT_ID = client_id
