from flask import Flask
from flask import request
import selenium_base
from selenium_base import Page
app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def starting():
    data = request.json
    lat =  data.get("lat")
    lon = data.get("lon")
    return Page.perform(str(lat),str(lon))

if __name__ == '__main__':
    app.run()