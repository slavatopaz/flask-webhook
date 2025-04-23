from flask import Flask, request

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
        print("Received:", data)

        # Прокидываем в Make (замени URL ниже)
        import requests
        requests.post('https://hook.make.com/your-make-webhook', json=data)

        return 'OK', 200

if __name__ == '__main__':
    app.run()
