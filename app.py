import hmac
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = '9148022055:AAGoqODYB5DqwJ0VYLZ1keREhDAdCzlHZo'
SIGNING_SECRET = '47ded207703a7af93f80'

@app.route('/', methods=['POST'])
def verify_webhook():
    signature = request.headers.get('X-IPRN-Signature')
    timestamp = request.headers.get('X-IPRN-Timestamp')
    if not signature or not timestamp:
        return 'Unauthorized', 401
    
    raw_body = request.get_data(as_text=True)
    message = f"{timestamp}.{raw_body}"
    expected_signature = hmac.new(
        SIGNING_SECRET.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    if hmac.compare_digest(expected_signature, signature):
        return jsonify({'status': 'verified'}), 200
    return 'Forbidden', 403

@app.route('/bot', methods=['POST'])
def bot_webhook():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
