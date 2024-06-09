from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a test Flask app!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Обработка данных
    return "Webhook received!", 200

if __name__ == '__main__':
    app.run(debug=True)
