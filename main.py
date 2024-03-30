import wget
from bs4 import BeautifulSoup
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

input_path = 'input'
output_path = 'output'


def get_html_list():
    _html_list = set()
    _htmls = os.listdir(input_path)
    for html in _htmls:
        _html_list.add(os.path.join(input_path, html))
    return _html_list


def get_links(_file_path):
    _got_links = set()
    with open(_file_path, 'r') as html:
        soup = BeautifulSoup(html, "html.parser")
        att_links = soup.findAll('a', class_="attachment__link")
        for link in att_links:
            if link['href'][8:11] == "sun":
                _got_links.add(link['href'])
    return _got_links


def download_links(_links, _download_path):
    for link in _links:
        wget.download(link, _download_path)


def download_all():
    pass


def get_all_links():
    _all_links = set()
    for html in get_html_list():
        _all_links.update(get_links(html))
    with open('links.txt', 'w') as f:
        for link in _all_links:
            f.write(str(link)+'\n')


if __name__ == "__main__":
    pass
    # get_all_links()
    #download_links()
