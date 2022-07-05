from app import application as app
import src.modules.shipment.service as a

@app.get('/')
def index():
    response = a.find()
    print(response)
    return response