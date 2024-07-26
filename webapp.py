from flask import Flask, request, jsonify, render_template_string
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization
import pyjokes

try:
    from flag import FLAG
except ImportError:
    FLAG = "flag{fake_flag_???????????}"

app = Flask(__name__)

public_key_pem = open("pubkey.pem").read()

# Load the public key
public_key = serialization.load_pem_public_key(public_key_pem.encode())

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <body>
        <form action="/verify" method="post">
            <label for="message">Message:</label><br>
            <input type="text" id="message" name="message"><br>
            <label for="signature">Signature (hex):</label><br>
            <input type="text" id="signature" name="signature"><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    ''')

@app.route('/verify', methods=['POST'])
def verify_signature():
    try:
        message = request.form['message'].encode()
        signature = bytes.fromhex(request.form['signature'])

        # Verify the signature
        public_key.verify(
            signature,
            message,
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        if b"gif flag" in message:
            return jsonify({"flag": FLAG})

        return jsonify({'joke': pyjokes.get_joke()})

    except Exception as e:
        return jsonify({'verified': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

