import requests
from bs4 import BeautifulSoup
import datetime

url="https://emrtds.nepalpassport.gov.np/iups-api/calendars/79/false"
response=requests.get(url)

api_content=response.text


today_date=datetime.datetime.now().isoformat()

with open(f'dap_{today_date}.json','w') as f:
    f.write(api_content)
