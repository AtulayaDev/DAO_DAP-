import requests
from bs4 import BeautifulSoup
import datetime

url="https://emrtds.nepalpassport.gov.np/iups-api/calendars/78/false"
response=requests.get(url)

api_content=response.text


    
# doc=BeautifulSoup(api_content,'html.parser')

today_date=datetime.datetime.now().isoformat()

# file_name=f"dao_{today_date}.json"

with open(f'dao_{today_date}.json','w') as f:
    f.write(api_content)

