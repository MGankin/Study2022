from btc_price.models import BitcoinCalculactor
import requests
import json

def run():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    text_json = requests.get(url).text
    bit_data =  json.loads(text_json)

    for curr in bit_data['bpi']:
        new_rate = bit_data['bpi'][curr]['rate']
        new_rate = new_rate.replace(',','')
        add_value = BitcoinCalculactor(currency = curr, rate = new_rate)
        add_value.save()
    print("Data Added")
