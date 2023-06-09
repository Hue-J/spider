from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from webdrivermanager.gecko import GeckoDriverManager

from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Firefox()
driver.get("https://www.fowaonsite.com/member_directory#!directory/map/ord=lnm")
for _ in range (25):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
results = soup.find_all("div", {"id" : "SFylpcrd"})
# Create empty list
member_list = []
for member in results:
    # Create empty dict
    data_dict = {}
    # Add title,url and metadata to the disctionary as keys
    member_script = member.find("a", {"class": "SFcrd"})
    name = [name for name in member_script.find('strong').children]
    data_dict['company_name'] = name[0]
    individual_name = name[2].split()
    data_dict['first_name'] = individual_name[0]
    data_dict['last_name'] = ' '.join(individual_name[1:])
    data_dict['phone_number'] = member_script.find_all("div")[1].text
    data_dict['street_address'] = member_script.find('span', {'itemprop': "streetAddress"}).text
    data_dict['address_locality'] = member_script.find('span', {'itemprop': "addressLocality"}).text

    # Append data to list
    member_list.append(data_dict)

    
# create dataframe to save the data according to the url
fowa_df = pd.DataFrame.from_dict(member_list)
fowa_df.to_csv("fow.csv", index = False)

