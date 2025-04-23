from flask import Flask, request
import requests
import json

app = Flask(__name__)
VERIFY_TOKEN = 'my_verify_token'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'Verification token mismatch', 403

    if request.method == 'POST':
        data = request.json
        print("🔥 Новое событие от Meta:", json.dumps(data, indent=2, ensure_ascii=False))

        # Отправка в Make
        requests.post(
            'https://hook.us2.make.com/cb3nu9327q1lzukvfwnu0m3nt7cgxvc0',
            json=data,
            headers={'Content-Type': 'application/json'}
        )

        return 'OK', 200

if __name__ == '__main__':
    app.run()
