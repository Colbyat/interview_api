from flask import Flask, send_from_directory
from flask_restful import Api
from api.GetDataHandler import GetDataHandler

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():  # put application's code here
    return send_from_directory("frontend/", "index.html")


api.add_resource(GetDataHandler, "/getdata")


if __name__ == '__main__':
    app.run()
