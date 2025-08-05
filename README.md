# AnonDrop Package

AnonDrop is a Python package that allows users to upload and delete files using the AnonDrop service. This package provides a simple interface for file management, making it easy to integrate file uploads into your applications.

## Features


- Upload files to AnonDrop with ease.
- Delete files from AnonDrop using their unique file ID.
- Simple and intuitive API.

## Installation

You can install and update the AnonDrop package using pip:

```
pip install --upgrade anondrop
```

## Usage

### Getting Client ID

Head to the <a href="https://anondrop.net/dashboard" target="_blank">AnonDrop Dashboard</a> and click your Client Key in the top left

### Uploading a File

To upload a file, you need to set your Client Key and call the `upload` function:

```python
import anondrop

anondrop.setClientKey('your_client_key_here') # anondrop.setClientID will soon be deprecated to match the website
file_path = 'path/to/tag.sk'
uploaded_file = anondrop.upload(file_path)

print(f"File URL: {uploaded_file.fileurl}")
# File URL: https://anondrop.net/1369090222146457662/tag.sk
print(f"File ID: {uploaded_file.fileid}")
# File ID: 1369090222146457662
print(f"URL: {uploaded_file.filepage}")
# File ID: https://anondrop.net/1369090222146457662
```

### Uploading a File Remotely

To upload a remote file, first have your Client Key set, then call the `remoteUpload` function:

```python
import anondrop

anondrop.setClientKey('your_client_key_here')
link = 'https://raw.githubusercontent.com/BubblePlayzTHEREAL/AnonDrop/refs/heads/main/setup.py'
uploaded_file = anondrop.remoteUpload(link)

print(f"File URL: {uploaded_file.fileurl}") # The url is not returned so this doesnt work.
# File URL: None
print(f"File ID: {uploaded_file.fileid}")
# File ID: 1378090451105484880
print(f"URL: {uploaded_file.filepage}")
# File ID: https://anondrop.net/1378090451105484880
```

### Deleting a File

To delete a file, use the `delete` function with the file ID:

```python
import anondrop

anondrop.setClientKey('your_client_key_here')
file_id = 'your_file_id_here'
anondrop.delete(file_id)
print("File deleted successfully.")
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
