import requests
import json
import pandas as pd
import time

api_key = ""

# Make a request
url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25136/dados?formato=json'

response = requests.get(url)

print(response.json())
