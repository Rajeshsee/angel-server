from flask import Flask, jsonify
from smartapi import SmartConnect
import pyotp

app = Flask(__name__)

@app.route('/angel-login', methods=['GET'])
def angel_login():
    api_key = "2ECIbSHz"
    client_id = "R62700940"
    password = "Rajesh054@"
    totp_secret = "BDTR4JNHBGJWXWE44PTDDP5BIA"

    try:
        obj = SmartConnect(api_key=api_key)
        totp = pyotp.TOTP(totp_secret).now()

        data = obj.generateSession(client_id, password, totp)
        return jsonify(data)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
