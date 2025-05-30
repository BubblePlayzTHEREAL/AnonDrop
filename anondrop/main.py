import requests
import re
from . import config


class UploadOutput:
    def __init__(self, filelink, link, fileid):
        self.fileurl = filelink
        self.filepage = link
        self.fileid = fileid


def upload(file_path, filename=None):
    if config.CLIENT_ID is None:
        raise ValueError("CLIENT_ID is not set. Please set it before uploading.")
    if filename is None:
        filename = file_path.split("/")[-1]
    with open(file_path, "rb") as file:
        b64_data = file.read()
    res = requests.get(
        f"https://anondrop.net/initiateupload?filename={filename}&key="
        + config.CLIENT_ID,
    )
    hash = res.text
    upload_url = "https://anondrop.net/uploadchunk?session_hash=" + hash
    files = {"file": ("blob", b64_data, "application/octet-stream")}
    res = requests.post(upload_url, files=files)
    link = None
    if res.text == "done":
        res = requests.get("https://anondrop.net/endupload?session_hash=" + hash)
        match = re.search(r"href='(.*?)'", res.text)
        if match:
            link = match.group(1)
        return UploadOutput(link + "/" + filename, link, link.split("/")[-1])
    else:
        raise Exception("Upload failed.")


def remoteUpload(url):
    if config.CLIENT_ID is None:
        raise ValueError("CLIENT_ID is not set. Please set it before uploading.")
    res = requests.get(
        f"https://anondrop.net/remoteuploadurl?key={config.CLIENT_ID}&url={url}&session_hash={config.CLIENT_ID}-{url}"
    )
    print("Response text:", res.text)  # Debugging line
    match = re.search(r"href='(.*?)'", res.text)
    if match:
        link = match.group(1)
        fileid = link.split("/")[-1]
        return UploadOutput(link, link, fileid)
    else:
        raise Exception("Remote upload failed.")


def delete(fileid):
    if config.CLIENT_ID is None:
        raise ValueError("CLIENT_ID is not set. Please set it before deleting.")
    res = requests.post(f"https://anondrop.net/delete/{fileid}?key=" + config.CLIENT_ID)
    if res.text == "deleted":
        return
    else:
        raise Exception("Delete failed.")
