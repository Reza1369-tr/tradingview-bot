
import requests
from flask import Flask, request

app = Flask(__name__)

# Replace these with your actual token and chat_id
TELEGRAM_TOKEN = '7030035075:AAE1-5ul4n9wtKbaHierA4GzSgBOtKbgCHo'
TELEGRAM_CHAT_ID = '6465751116'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'No message received')
    
    telegram_url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    
    response = requests.post(telegram_url, data=payload)
    return {'status': 'sent', 'telegram_response': response.json()}

if __name__ == '__main__':
    app.run(debug=True)
