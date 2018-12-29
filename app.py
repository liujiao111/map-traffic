from flask import Flask, request, render_template
from flask import render_template
import json

import TrafficDataController

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/traffic', methods=['GET', 'POST'])
def traffic():
    #retangle_value = request.form['retangle_value']
    #retangle_value = request.values.get('retangle_value')
    retangle_value = request.args.get('retangle_value')

    print('矩形：', retangle_value)
    circle_value = request.args.get('circle_value')
    road_value = request.args.get('road_value')

    if(retangle_value is not None):
        rectangle_params = {
            'rectangle': retangle_value
        }
        data = TrafficDataController.getTrafficData('rectangle', rectangle_params)
    elif retangle_value is not None:
        circle_params = circle_value
        data = TrafficDataController.getTrafficData('circle', circle_params)
    else:
        road_params = road_value
        data = TrafficDataController.getTrafficData('road', road_params)

    return json.dumps(data)

@app.route('/test', methods=['GET', 'POST'])
def test():
    return json.dumps("{'s':'1','d':'e'}")


if __name__ == '__main__':
    app.run()