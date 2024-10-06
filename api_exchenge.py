import requests
from tok import currency_token


def get_rate_usd() -> float:
    try:
        try:
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            if response.status_code == 200:
                value = response.json()
                return round(value['Valute']['USD']['Value'], 2)
        except:
            url = "https://api.apilayer.com/fixer/convert?to=RUB&from=USD&amount=1"
            payload = {}
            headers = {"apikey": currency_token}
            response = requests.request("GET", url, headers=headers, data=payload)
            if response.status_code == 200:
                value = response.json()
                return round(value['info']['rate'], 2)
    except:
        return 'Сервис временно не доступен!'



