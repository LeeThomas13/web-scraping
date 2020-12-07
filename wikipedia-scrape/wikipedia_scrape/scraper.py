import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Chess'


def get_citations_needed_count(url):
    #takes in url and returns an integer

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(title='Wikipedia:Citation needed')
    counter = 0

    for cites_needed in results:
        counter += 1
    get_citations_needed_report(counter)

def get_citations_needed_report(integer):
    #takes in an integer and returns a string
    print(f'There are {integer} needed citations for this wiki page')

get_citations_needed_count(url)
