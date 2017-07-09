from multiprocessing import pool
import random
import string
import requets
import bs4 as bs

def random_starting_url():
	starting = ''.join(random.systemrandom().choice(string.ascii_lowercase) for _ in range(3))
	url = ''.join(['http://', starting, '.com'])
	return url

def handle_local_links(url,links):
	if link.startswith('/'):
		return (''.join([url,link]))
	else:
		return link

def get_links(url):
	try:
		resp = request.get(url)
		soup = bs.BeautifulSoup(resp.text, 'lxml')
		body = soup.body
		links = [link.get('href') for link in body.find_all('a')
		links = [handle_local_links(url,link) for link in links]
		links = [str(link.encode("ascii")) for link in links]

	
	except TypeError as e:
		print(e)
		print('got a None that we tried to iterarte over')
		return []

	except IndexError as e:
		print(e)
		print('probably no useful links found, returning empty list')
		return []

	except AttributeError as e:
		print(e)
		print('Likely got None for links so we are here')
		return []

	except Exception as e:
		print(str(e))
		return[]


def main():
	how_many = 25
	p = Pool(processes = how_many)
	parse_us = [random_starting_url() for _ in range(how_many)]
	data = p.map(get_links [link for link in parse_us])
	data = [url for url_list 