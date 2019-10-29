from typing import List

from DataClasses.RouteDataClass import Route, Step
import dataclasses

from GoogleMaps import Direction
from GoogleMaps import tsp

from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return jsonify({'message': 'Hello, world'})

@app.route('/routes')
def get_toure():
    waypoints = ['五稜郭タワー', 'ラッキーピエロ+美原店', 'ラーメン炙+五稜郭店']
    routes: [Route] = Direction.get_routes("五稜郭駅", "函館駅", "2019/11/25 12:00", waypoints)
    for a in routes:
        print(a.id)
        print(dataclasses.asdict(a))

    return "hello"


if __name__ == '__main__':
    app.run(debug=True)

