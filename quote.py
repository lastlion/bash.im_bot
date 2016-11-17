import urllib2
from bs4 import BeautifulSoup
import random


def get_quote():
    rand = random.randint(1, 10000)
    url = 'http://bash.im/random?' + str(rand)
    headers = {'User-Agent': 'Mozilla/5.0'}

    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html)
    div_quote = soup.find("div", class_='quote')
    quote_id = div_quote.find('a', class_='id')
    div_text = div_quote.find("div", class_='text')
    id = quote_id.get_text()
    text = div_text.encode_contents()
    text = text.replace('<br>', '\n')
    text = text.replace('</br>', '')
    soup = BeautifulSoup(text)
    text = soup.get_text()

    return [id[1:], text]
