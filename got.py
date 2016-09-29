from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'
response = urlopen(url).read()
soup = BeautifulSoup(response)
links = soup.findAll("a")

viewers = {}

for season in range(1, 8):
    for link in links:
        if link.string == "Season " + str(season):
            got_url = "https://en.wikipedia.org" + link["href"]
            got_html = urlopen(got_url).read()
            got_soup = BeautifulSoup(got_html)

            rows = got_soup.findAll("tr", attrs={"class" : "vevent"})

            viewerSum = 0
            for row in rows:
                cells = row.findAll(recursive=False)
                viewerSum += float(cells[-1].contents[0])

            viewers[season] = viewerSum
            break

print viewers