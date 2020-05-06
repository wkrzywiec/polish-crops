import tools.data_helper as helper

__raw_data_directory = 'data/raw/'
__crop_prices_url = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=data/apri_ap_crpouta.tsv.gz'
__crop_categories_url = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=dic/en/prod_veg.dic'

def download_crop_prices():
    """Download & unzip 'Selling prices of crop products (absolute prices) - annual price (from 2000 onwards)' report - apri_ap_crpouta.tsv

    Returns:
        str -- path to saved file
    """
    content = helper.download_file(__crop_prices_url)
    file_name = __crop_prices_url.split('/')[-1]
    zipped_file_path = helper.save_file(content, __raw_data_directory + file_name)
    unzipped_file = helper.unzip_gz_file(zipped_file_path)
    helper.delete_file(zipped_file_path)
    return unzipped_file
    
def download_crop_categories_dic():
    """Download crop categories dictionary - prod_veg.dic

    Returns:
        str -- path to saved file
    """
    content = helper.download_file(__crop_categories_url)
    file_name = __crop_categories_url.split('/')[-1]
    raw_file_path = helper.save_file(content, __raw_data_directory + file_name)
    return raw_file_path