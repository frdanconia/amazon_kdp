from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_titles_from_author_site(url):
    with urlopen(url) as url:
        """Function to find KDP publication titles using author central url"""
        bs = BeautifulSoup(url.read(), 'html.parser')
        titles_author = bs.select('span.a-size-medium')
        titles = [t.text for t in titles_author]
        return titles


kdp_url = "https://www.amazon.com/FONAJ-studio/e/B07XSM3Q3Z?ref=sr_ntt_srch_lnk_1&qid=1595074812&sr=8-1"
print(get_titles_from_author_site(kdp_url))
