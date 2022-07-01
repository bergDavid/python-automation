import requests

def apicollectprice(symbol):
    url = "https://yfapi.net/v7/finance/options/XPLG11.SA"
    payload={}
    headers = {
    'X-API-KEY': 'OzSm0eWTFK37aCA2YaQRs2szoXcz0pcq90Vf4ivz',
    'Accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.text
    else:
        return "error"
