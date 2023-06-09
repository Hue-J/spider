'''
This is a script meant to scrap videos from any youtube channel from the videos tab.
The data to be collected os the channel name which is udes to name the csv file, video
title, video url, number of views and the period that has passed since it was uploaded. 
The data is then saved to a csv file.
'''
# import required drivers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager
# from webdrivermanager.gecko import GeckoDriverManager

from bs4 import BeautifulSoup
import time
import pandas as pd

# create wedriver object

# driver = webdriver.Chrome() # for chrome users

driver = webdriver.Firefox()

# get url for example https://www.youtube.com/@little_soul/videos
url = input("Enter the youtube url channel you want to scrap: ")
driver.get(url)

# load the whole page 
for _ in range (50):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)
# get html page source to use for scrapping
html = driver.page_source

#  create beutiful soup object and parse html
soup = BeautifulSoup(html, 'html.parser')

# chanel_name = soup.find_all("div", {"id": 'text-container'})
chanel_name = soup.find("yt-formatted-string", {"id": 'channel-handle'}).text
save_name = chanel_name.replace('@','')
videos = soup.find_all("div", {"id" : "dismissible"})
# print(chanel_name)
# Create empty list
video_list = []
for video in videos:
    # Create empty dict
    data_dict = {}
    # Add title,url and metadata to the disctionary as keys
    data_dict['title'] = video.find("a", {"id":"video-title-link"}).text
    data_dict["video_url"] = "https://www.youtube.com" + video.find("a", {"id":"video-title-link"})["href"]
    
    meta = video.find("div", {"id":"metadata-line"}).find_all("span")
    data_dict["views"] = meta[0].text
    data_dict["period"] = meta[1].text

    # Append data to list
    video_list.append(data_dict)
    
# create dataframe to save the data according to the url
youtube_df = pd.DataFrame.from_dict(video_list)
youtube_df.to_csv(f"{save_name}.csv", index = False)
