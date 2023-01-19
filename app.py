from flask import Flask


def create_app():
    app = Flask(__name__)

    stores = [{"name": "My Store", "items": [
        {"name": "my item", "price": 15.99}]}]

    @app.get("/fedor")
    def get_stores():
        return {"stores": stores}
