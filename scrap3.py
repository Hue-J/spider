''' 
Some websites built in javascript and django cannot be scrapped using the request
module. Request is only applicable for the webpages that return xml or html.
For those that do not return html you need selenium module which opens the 
page the same way as the browser making the html available.

BELOW IS AN EXAMPLE OF A WEBSITE THAT IS DIFFICULT TO SCRAP USING REQUEST LIBRARY.
'''

import requests
from bs4 import BeautifulSoup

# import images from pngmart.com
# 'https://www.pngegg.com/'
# url = input('Enter url: ')
url = "https://www.nordstrom.com/brands/steve-madden--469"
response = requests.get(url, timeout= (2,5))
html = response.content
headers = response.headers
print(headers)

# html = BeautifulSoup(response.text, 'html.parser')
# content = html.find_all("div", {"class": "DSQCI"})
# list = html.find_all('li')
# print(len(list))

# site_map = []
# for loc in html.find_all('loc'):
#     site_url = loc.text
#     if  'part' in site_url:
#         site_map.append[site_url]
#         print (site_map)


