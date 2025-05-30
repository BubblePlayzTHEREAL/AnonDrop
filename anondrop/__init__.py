from .main import upload, delete, remoteUpload, UploadOutput
from . import config


def setClientID(client_id: str):
    config.CLIENT_ID = client_id
