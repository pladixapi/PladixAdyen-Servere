import web
import json
from encryptor import encryptor  # Certifique-se de que a classe encryptor esteja no mesmo diretório ou instalada como um pacote
from web.wsgiserver import CherryPyWSGIServer

urls = ("/encrypt", "Encrypt")

class Encrypt:
    def POST(self):
        try:
            data = json.loads(web.data())
            
            adyen_key = data.get("adyen_key", "null")  # Chave Adyen
            adyen_version = data.get("adyen_version", "_0_1_8")  # Versão Adyen
            
            card = data.get("card")
            cvv = data.get("cvv")
            month = data.get("month")
            year = data.get("year")
            
            # Inicializando o encryptor com a chave e a versão fornecidas
            enc = encryptor(adyen_key, adyen_version=adyen_version)
            encrypted_data = enc.encrypt_card(card, cvv, month, year)
            
            return json.dumps({"success": True, "data": encrypted_data})
        
        except Exception as e:
            return json.dumps({"success": False, "error": str(e)})

print("Configuring web.py application...")
app = web.application(urls, globals())
print("Application configured, ready to run.")

if __name__ == "__main__":
    print("Starting CherryPyWSGIServer on port 443")
    CherryPyWSGIServer.ssl_certificate = "/path/to/your/certificate.pem"
    CherryPyWSGIServer.ssl_private_key = "/path/to/your/privatekey.pem"
    app.run(port=443)
    print("Server is running on port 443")
