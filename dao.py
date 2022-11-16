import requests
from bs4 import BeautifulSoup

url="https://emrtds.nepalpassport.gov.np/iups-api/calendars/78/false"
response=requests.get(url)

api_content=response.text

with open('api_dao.json','w') as f:
    f.write(api_content)
    
doc=BeautifulSoup(api_content,'html.parser')

offdates_date= doc.find("offDates")
print(offdates_date)

