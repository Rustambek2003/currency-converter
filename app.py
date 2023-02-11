from flask import Flask, request
import requests

app = Flask(__name__)

def get_data():
    response = requests.get('https://nbu.uz/uz/exchange-rates/json/')
    r = response.json()[-1]
    global usd
    usd = float(r['nbu_buy_price'])
    

get_data()

@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    args = request.args
    amount = float(args.get('amount',0))
    print(amount)

    return {
        "amount": amount,
        "currency": "UZS",
        "converted": round(amount/usd,2),
        "convertedCurrency": "USD"
    }

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """

    args = request.args
    amount = float(args.get('amount',0))
    print(amount)
    return {
        "amount": amount,
        "currency": "USD",
        "converted": round(amount*usd,2),
        "convertedCurrency": "UZS"
    }



if __name__ == '__main__':
    app.run()    