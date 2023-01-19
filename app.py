from flask import Flask
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    load_dotenv()

    stores = [{"name": "My Store", "items": [
        {"name": "my item", "price": 15.99}]}]

    @app.get("/fedor")
    def get_stores():
        return {"stores": stores}

    return app
