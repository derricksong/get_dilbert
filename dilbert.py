#!/usr/bin/env python3
"""
  Dilbert.  With python3
  root@derricksong.com
"""


import requests
from bs4 import BeautifulSoup

dilbert_url = 'https://www.dilbert.com'

def main():
	comic_url = get_comic(dilbert_url)
	return

	
def get_comic(url):

	try:
		r = requests.get(url)
	except Exception as e:
		print(f'Error! {e}')

	_soup = BeautifulSoup(_r.content, 'html.parser')
	_comic = _soup.find("div", {
		'class': 'img-comic-container'
	})
	_url = f'https:{_comic.img['src']}'

	return _url


def build_html():

	return


if __name__ == "__main__":
	main()
