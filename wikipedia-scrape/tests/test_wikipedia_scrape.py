from wikipedia_scrape import __version__
from wikipedia_scrape.scraper import get_citations_needed_count, get_citations_needed_report


def test_version():
    assert __version__ == '0.1.0'

def test_one_citation():
    url = 'https://en.wikipedia.org/wiki/Chess'
    actual = get_citations_needed_count(url)
    expected = 'There are 1 needed citations for this wiki page'
    assert actual == expected

def test_many_citations():
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_count(url)
    expected = 'There are 7 needed citations for this wiki page'
    assert actual == expected