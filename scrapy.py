'''
Web Scraping - URL and Email IDs
'''

#import required libraries
import urllib.request
from bs4 import BeautifulSoup

#URL to Scrap
wiki = "https://dlca.logcluster.org/display/public/DCLA/4.1+Nepal+Government+Contact+List"

#Query the website to return the url to the variable <name>
pge = urllib.request.urlopen(wiki)

#Parse the variable and store in BeautifulSoup format
soup = BeautifulSoup(pge, features = 'html.parser')

title = soup.title.string
all_links = soup.find_all('a')


if len (all_links) > 5:
    last_5 = all_links[len(all_links)-5:]
    for url in last_5:
        print(url.get('href'))

emails = []
for url in all_links :
    if (str(url.get('href')).find('@') > 0):
        emails.append(url.get('href'))

for email in emails [:5]:
    print(email)
print("Total number of emails found is:", len(emails)) 
