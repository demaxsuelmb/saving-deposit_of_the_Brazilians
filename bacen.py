import requests
import json
import pandas as pd
import time

# Make a request
# Saldo poupança
url_100 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25135/dados?formato=json'
url_500 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25136/dados?formato=json'
url_1000 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25137/dados?formato=json'
url_2000 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25138/dados?formato=json'
url_5000 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25139/dados?formato=json'
url_10000 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25140/dados?formato=json'
url_15000 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25141/dados?formato=json'
url_20000 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25142/dados?formato=json'
url_25000 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25143/dados?formato=json'
url_30000 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25144/dados?formato=json'
url_more_30000 = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.25145/dados?formato=json'


# # Export data less than 100 to csv
# dados_100 = pd.read_json(url_100)
# dados_100.to_csv('dados_100.csv')

# # Export data less than 500 to csv
# dados_500 = pd.read_json(url_500)
# dados_500.to_csv('dados_500.csv')

# Export data less than 1000 to csv
dados_1000 = pd.read_json(url_1000)
dados_1000.to_csv('dados_1000.csv')

# Export data less than 2000 to csv
dados_2000 = pd.read_json(url_2000)
dados_2000.to_csv('dados_2000.csv')

# Export data less than 5000 to csv
dados_5000 = pd.read_json(url_5000)
dados_5000.to_csv('dados_5000.csv')

# Export data less than 10000 to csv
dados_10000 = pd.read_json(url_10000)
dados_10000.to_csv('dados_10000.csv')

# Export data less than 15000 to csv
dados_15000 = pd.read_json(url_15000)
dados_15000.to_csv('dados_15000.csv')

# Export data less than 20000 to csv
dados_20000 = pd.read_json(url_20000)
dados_20000.to_csv('dados_20000.csv')

# Export data less than 25000 to csv
dados_25000 = pd.read_json(url_25000)
dados_25000.to_csv('dados_25000.csv')

# Export data less than 30000 to csv
dados_30000 = pd.read_json(url_30000)
dados_30000.to_csv('dados_30000.csv')

# # Export data bigger than 3000 to csv 
dados_3000 = pd.read_json(url_more_30000)
dados_3000.to_csv('dados_more_3000.csv')
