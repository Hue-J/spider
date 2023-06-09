import requests
from bs4 import BeautifulSoup

#Inquire the URL  to be scraped
#For this we use https://pythonjobs.github.io/
URL = input('Enter the URL you want to scrap:') 
#Retrieve html data using the request library
page = requests.get(URL)

#Parse the html data to BeutifulSoup and create new object
soup = BeautifulSoup(page.content, 'html.parser')

#FInd element by ID
results = soup.find(class_='card-deck')

#Narrow down the results
developer_jobs = results.find_all("h6", string= lambda text: "stack" in text.lower())
print (len(developer_jobs))
#job_elements = results.find_all("div", class_ = "card-content")
#Get the parent after filtering the  job listings
job_elements = [span_element.parent.parent for span_element in developer_jobs]

for job_element in job_elements:
    title_element = job_element.find("p", class_="m-0")
    company_element = job_element.find("p", class_="text-secondary")
    location_element = job_element.find("small")
    
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
