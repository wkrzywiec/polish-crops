import os
import tools.data_helper as helper

__raw_data_directory = 'data/raw/'

def download_crop_prices(url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=data/apri_ap_crpouta.tsv.gz"):
    """Download & unzip 'Selling prices of crop products (absolute prices) - annual price (from 2000 onwards)' report from Eurostat

    Keyword Arguments:
        url {str} -- URL of a report (default: {"https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=data/apri_ap_crpouta.tsv.gz"})

    Returns:
        str -- path to saved file
    """
    content = helper.download_file(url)
    file_name = url.split('/')[-1]
    zipped_file_path = helper.save_file(content, __raw_data_directory + file_name)
    unzipped_file = helper.unzip_gz_file(zipped_file_path)
    os.remove(zipped_file_path)
    return unzipped_file
    
def download_crop_categories_dic(url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=dic/en/prod_veg.dic"):
    """Download crop categories dictionary

    Keyword Arguments:
        url {str} -- URL of a dictionary (default: {"https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=dic/en/prod_veg.dic"})

    Returns:
        str -- path to saved file
    """
    content = helper.download_file(url)
    file_name = url.split('/')[-1]
    raw_file_path = helper.save_file(content, __raw_data_directory + file_name)
    return raw_file_path