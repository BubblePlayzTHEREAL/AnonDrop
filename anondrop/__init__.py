from .main import upload, delete, UploadOutput


def setClientID(client_id: str):
    global CLIENT_ID
    CLIENT_ID = client_id
