import wget
from bs4 import BeautifulSoup
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

input_path = 'input'
output_path = 'output'


def date_fmt(_date):
    "Серафим Казачков, 19 авг 2023 в 7-32-44"
    _spt1 = _date.split(', ')
    _name = _spt1[0]
    _spt_date = _spt1[1].split(' ')
    _new_date = f"{_spt_date[2]} {_spt_date[1]} {_spt_date[0]} {_spt_date[-1]} ({_name})"
    return _new_date


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
        att_links = soup.findAll('div', class_="message")
        att_links = [link for link in att_links if link.find('a', class_="attachment__link")]
        for link in att_links:
            _href = str(link.find('a', class_="attachment__link")['href'])
            if _href[8:11] == "sun":
                _date = date_fmt(link.find('div', class_="message__header").text)
                _got_links.add((_href, _date))
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
            f.write(link[0]+', '+link[1]+'\n')


if __name__ == "__main__":
    get_all_links()
    #download_links()
