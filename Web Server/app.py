from HitCountAPI import *
from flask import Flask
from flask_restful import Api
from config import LocalDevelopmentConfig
from flask_cors import CORS

# from flask_caching import Cache
# from waitress import serve

app = None
api = None
cache = None


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)

    CORS(app)
    app.app_context().push()

    api = Api(app)
    app.app_context().push()

    # cache = Cache(app)
    # app.app_context().push()

    return app, api, cache


app, api, cache = create_app()


api.add_resource(HitCountAPI, "/api/hit")

if __name__ == '__main__':
    app.run(processes=2, threaded=False)
