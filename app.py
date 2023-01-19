from flask import Flask
import os
from dotenv import load_dotenv


def create_app():

    app = Flask(__name__)

    load_dotenv()
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    stores = [
        {
            "name": "My Store",
            "items": [
                {
                    "name": "Chair",
                    "price": 15.99
                }
            ]
        }
    ]

    @app.get("/")
    def get_stores():
        return {"stores": stores}

    return app
