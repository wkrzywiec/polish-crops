import requests
import gzip
import os

__raw_data_directory = 'data/raw/'

def download_crop_prices(url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=data/apri_ap_crpouta.tsv.gz"):
    content = __download_file(url)
    file_name = url.split('/')[-1]
    zipped_file_path = __save_file(content, __raw_data_directory + file_name)
    unzipped_file = __unzip_gz_file(zipped_file_path)
    os.remove(zipped_file_path)
    return unzipped_file
    
def download_crop_categories_dic(url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=dic/en/prod_veg.dic"):
    content = __download_file(url)
    file_name = url.split('/')[-1]
    raw_file_path = __save_file(content, __raw_data_directory + file_name)
    return raw_file_path

def __download_file(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise SystemExit('Unable to download data file. Reason: {} {}'.format(response.status_code, response.reason))
    return response.content

def __save_file(content, file_path: str) -> str:
    with open(file_path, 'wb') as f: 
        f.write(content)
    return file_path

def __unzip_gz_file(file_path):
    gz_extension_index = file_path.rfind('.')
    unziped_file_path = file_path[:gz_extension_index]
    with gzip.open(file_path, 'rb') as f:
        __save_file(f.read(), unziped_file_path)
    return unziped_file_path
    