from flask import Flask, render_template, request, send_file
from Crypto.Cipher import AES
import os

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Encrypt route
@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    uploaded_file = request.files['file']
    key = request.form['key'].encode('utf-8')

    # Pad key to 16 bytes
    key = key.ljust(16, b'0')

    # Read and encrypt data
    data = uploaded_file.read()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # Save encrypted file
    with open('encrypted_file.bin', 'wb') as f:
        f.write(cipher.nonce + tag + ciphertext)

    return send_file('encrypted_file.bin', as_attachment=True)

# Decrypt route
@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    uploaded_file = request.files['file']
    key = request.form['key'].encode('utf-8')

    # Pad key to 16 bytes
    key = key.ljust(16, b'0')

    # Read encrypted data
    data = uploaded_file.read()
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)

    with open('decrypted_file.txt', 'wb') as f:
        f.write(decrypted)

    return send_file('decrypted_file.txt', as_attachment=True)

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
