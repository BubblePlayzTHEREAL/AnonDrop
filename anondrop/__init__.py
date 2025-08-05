from .main import upload, delete, remoteUpload, UploadOutput
from . import config
import warnings


def setClientKey(client_key: str):
    config.CLIENT_KEY = client_key


def setClientID(client_id: str):
    warnings.warn(
        "setClientID will soon be deprecated, use setClientKey instead",
        DeprecationWarning,
        stacklevel=2,
    )
    config.CLIENT_KEY = client_id
