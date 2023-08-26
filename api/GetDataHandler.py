from flask_restful import Resource
import requests
from urllib.parse import urlparse
import utilities.Utils as utils


class GetDataHandler(Resource):

    def get(self):
        url = "https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json"
        url_id = urlparse(url).path
        select_val = utils.grabfromdb(url_id)
        if select_val is None:
            data = requests.get(url).json()
            csv = utils.verticaljsontopandasdf(data).to_csv()
            utils.savecsvtodb(url_id, csv)
            print("Saved to database")
        else:
            csv = select_val
            print("Grabbed from database")
        return csv

    get.__doc__ = "Grabs data from the static URL and returns a Json of the given data."
