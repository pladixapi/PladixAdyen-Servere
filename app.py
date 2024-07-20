from flask import Flask, request, jsonify
import json
from encryptor import encryptor

app = Flask(__name__)

@app.route(/encrypt, methods=[POST])
def encrypt():
    try:
        data = request.get_json()
        
        adyen_key = data.get("adyen_key", "null")
        adyen_version = data.get("adyen_version", "_0_1_8")
        
        card = data.get("card")
        cvv = data.get("cvv")
        month = data.get("month")
        year = data.get("year")
        
        enc = encryptor(adyen_key, adyen_version=adyen_version)
        encrypted_data = enc.encrypt_card(card, cvv, month, year)
        
        return jsonify({"success": True, "data": encrypted_data})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host=0.0.0.0)
