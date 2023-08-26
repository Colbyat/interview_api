from flask_restful import Resource
import requests


class GetDataHandler(Resource):

    def get(self):
        url = "https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json"
        data = requests.get(url).json()
        return data

    get.__doc__ = "Grabs data from the static URL and returns a Json of the given data."
