import requests
import gzip

def download_file(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise SystemExit('Unable to download data file. Reason: {} {}'.format(response.status_code, response.reason))
    return response.content

def save_file(content, file_path: str) -> str:
    with open(file_path, 'wb') as f: 
        f.write(content)
    return file_path

def unzip_gz_file(file_path):
    gz_extension_index = file_path.rfind('.')
    unziped_file_path = file_path[:gz_extension_index]
    with gzip.open(file_path, 'rb') as f:
        save_file(f.read(), unziped_file_path)
    return unziped_file_path