'''
The code gets data from the webpage https://realpython.github.io/fake-jobs/ 
The idea is to find specific jjobs from the website by utilizing the lambda 
function to specify the string literal.
'''
# Import required modules to be used.
import requests
from bs4 import BeautifulSoup

#Inquire the URL  to be scraped
#For this we use https://realpython.github.io/fake-jobs/
URL = input('Enter the URL you want to scrap:') 
#Retrieve html data using the request library
page = requests.get(URL)

#Parse the html data to BeutifulSoup and create new object
soup = BeautifulSoup(page.content, 'html.parser')

#Find element by ID
results = soup.find(id='ResultsContainer')

#Narrow down the results
developer_jobs = results.find_all("h2", string= lambda text: "engineer" in text.lower())
print (len(developer_jobs))
#job_elements = results.find_all("div", class_ = "card-content")
#Get the parent after filtering the  job listings
job_elements = [h2_element.parent.parent.parent for h2_element in developer_jobs]

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    #There are two ways to get the elements in the class     

#     title_element = job_element.find("h2", {'class' : "title"})
#     company_element = job_element.find("h3",{ 'class': "company"})
#     location_element = job_element.find("p", {'class': "location"})
    
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
