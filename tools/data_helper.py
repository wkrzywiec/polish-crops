import requests
import os
import gzip
from zipfile import ZipFile

def download_file(url: str):
    """Download file from provided URL

    Arguments:
        url {str} -- file's URL

    Raises:
        SystemExit: is raised when incorrect URL is provided

    Returns:
        [type] -- content of downloaded file
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise SystemExit('Unable to download data file. Reason: {} {}'.format(response.status_code, response.reason))
    return response.content

def save_file(content, file_path: str) -> str:
    """Save file in a directory

    Arguments:
        content {[type]} -- file content
        file_path {str} -- target path where file will be saved

    Returns:
        str -- path to saved file
    """
    with open(file_path, 'wb') as f: 
        f.write(content)
    return file_path

def delete_file(file_path: str):
    """Remove file

    Arguments:
        file_path {str} -- path of a file to be removed
    """
    os.remove(file_path)

def unzip_gz_file(file_path: str) -> str:
    """Extract file from .gz file

    Arguments:
        file_path {str} -- path to .gz file

    Returns:
        str -- path of unziped file
    """
    gz_extension_index = file_path.rfind('.')
    unziped_file_path = file_path[:gz_extension_index]
    with gzip.open(file_path, 'rb') as f:
        save_file(f.read(), unziped_file_path)
    return unziped_file_path

def unzip_zip_file(file_path: str) -> str:
    """Extract file from .zip file

    Arguments:
        file_path {str} -- path to .zip file

    Returns:
        str -- path of unziped file
    """
    zip_folder_index = file_path.rfind('/')
    unzip_target_folder = file_path[:zip_folder_index]
    unzipped_file_path = ''
    with ZipFile(file_path) as zip:
        unzipped_file_path = unzip_target_folder + '/' + zip.namelist()[0]
        zip.extractall(path=unzip_target_folder)
    return unzipped_file_path