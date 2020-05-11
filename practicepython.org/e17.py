''' https://www.practicepython.org/ 
Use the BeautifulSoup and requests Python packages to print out a list of all 
the article titles on the New York Times homepage.
'''
import requests
from bs4 import BeautifulSoup


def scraper(url):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'html.parser')
  out = soup.find_all('h2')
  count=1
  for i in out:
    print("{} {}".format(count,i))
    count+=1
  return ""

if __name__ == "__main__":
  url = "https://www.nytimes.com"
  print(scraper(url))
 