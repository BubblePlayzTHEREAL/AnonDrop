import requests
import re
from . import config


class UploadOutput:
    def __init__(self, filelink, link, fileid):
        self.fileurl = filelink
        self.filepage = link
        self.fileid = fileid


def chunks(file_name, size):
    with open(file_name, "rb") as f:
        while content := f.read(int(size * 1000000)):
            yield content


def upload(file_path, filename=None, chunksize=8):
    if config.CLIENT_KEY is None:
        raise ValueError("CLIENT_KEY is not set. Please set it before uploading.")
    if filename is None:
        filename = file_path.split("/")[-1]
    res = requests.get(
        f"https://anondrop.net/initiateupload?filename={filename}&key="
        + config.CLIENT_KEY,
    )
    hash = res.text
    file_chunks = list(chunks(file_path, chunksize))
    upload_url = "https://anondrop.net/uploadchunk?session_hash=" + hash
    for chunk in file_chunks:
        files = {"file": ("blob", chunk, "application/octet-stream")}
        res = requests.post(upload_url, files=files)
        if res.text != "done":
            raise Exception(
                "Chunk #"
                + (file_chunks.index(chunk) + 1)
                + " out of "
                + (len(file_chunks) + 1)
                + " failed."
            )
    link = None
    res = requests.get("https://anondrop.net/endupload?session_hash=" + hash)
    match = re.search(r"href='(.*?)'", res.text)
    if match:
        link = match.group(1)
    return UploadOutput(link + "/" + filename, link, link.split("/")[-1])


def remoteUpload(url):
    if config.CLIENT_KEY is None:
        raise ValueError("CLIENT_KEY is not set. Please set it before uploading.")
    res = requests.get(
        f"https://anondrop.net/remoteuploadurl?key={config.CLIENT_KEY}&url={url}&session_hash={config.CLIENT_KEY}-{url}"
    )
    print("Response text:", res.text)  # Debugging line
    match = re.search(r"href='(.*?)'", res.text)
    if match:
        link = match.group(1)
        fileid = link.split("/")[-1]
        return UploadOutput(None, link, fileid)
    else:
        raise Exception("Remote upload failed.")


def delete(fileid):
    if config.CLIENT_KEY is None:
        raise ValueError("CLIENT_KEY is not set. Please set it before deleting.")
    res = requests.post(
        f"https://anondrop.net/delete/{fileid}?key=" + config.CLIENT_KEY
    )
    if res.text == "deleted":
        return
    else:
        raise Exception("Delete failed.")
