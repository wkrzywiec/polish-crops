import tools.data_helper as helper

__base_url = 'https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/miesieczne/'
__precipitation_file_name_pattern = '{}_m_o.zip'
__raw_data_directory = 'data/raw/'

def download_precipitation_reports(years: list) -> dict:
    """Download precipitation reports from IMGW database

    Arguments:
        years {list} -- list of years for which to download reports

    Returns:
        dict -- dictionary of saved reports, where key = year, value = path_to_report
    """
    reports = {}
    for year in years:
        content = __download_zipped_file('opad', year)
        zipped_file_path = helper.save_file(content, __raw_data_directory + __precipitation_file_name_pattern.format(str(year)))
        unzipped_file_path = helper.unzip_zip_file(zipped_file_path)
        reports[year] = unzipped_file_path
        helper.delete_file(zipped_file_path)
    return reports


def download_temperature_reports(years: list):
    pass

def __download_zipped_file(type: str, year: int):
    return helper.download_file(__base_url + type + '/' + str(year) + '/' + __precipitation_file_name_pattern.format(str(year)))
