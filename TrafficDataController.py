from urllib.parse import quote
from urllib import request
import json
import xlwt
import time

AMAP_TRAFFIC_DATA_BASE_URL = 'https://restapi.amap.com/v3/traffic/status/'

AMAP_WEB_API_KEY = '930433cddfe95996550f42235c0095cc'


def getTrafficData(type, params):

    '''
    高德地图-根据类型获取交通态势数据
    API链接地址：https://lbs.amap.com/api/webservice/guide/api/trafficstatus#road
    :param type: 范围类型，可选项：
                            rectangle，矩形
                            circle， 圆形区域
                            road：指定线路交通态势
    :param params:请求参数
    :return:
    '''

    if(type == 'rectangle') :
        #矩形范围
        #示例URL：https://restapi.amap.com/v3/traffic/status/rectangle?rectangle=116.351147,39.966309;116.357134,39.968727&key=<用户的key>
        url = AMAP_TRAFFIC_DATA_BASE_URL + 'rectangle'
        if params == None or params['rectangle'] == None:
            return {
            'code' : '1',
            'msg' : '请传入矩形范围的两个对角点坐标！',
            'data' : {

            }
        }

        url = url + '?rectangle=' + params['rectangle'] + '&key=' + AMAP_WEB_API_KEY

        print('矩形范围，url:' + url)

        data = ''
        with request.urlopen(url) as f:
            data = f.read()
            data = data.decode('utf-8')
            print('圆形范围，高德返回数据:' + data)

        return {
            'code' : '0',
            'msg' : '成功！',
            'data' : data
        }

    elif (type == 'circle') :
        #圆形范围
        #示例URL：https://restapi.amap.com/v3/traffic/status/circle?location=116.3057764,39.98641364&radius=1500&key=<用户的key>
        url = AMAP_TRAFFIC_DATA_BASE_URL + 'circle'
        url = url + '?location=' + params['location'] + '&radius=' + params['radius'] + '&key=' + AMAP_WEB_API_KEY

        print('圆形范围，url:' + url)

        data = ''
        with request.urlopen(url) as f:
            data = f.read()
            data = data.decode('utf-8')
            print('圆形范围，高德返回数据:' + data)

        return {
            'code': '0',
            'msg': '成功！',
            'data': data
        }


    elif (type == 'road') :
        #指定线路交通态势
        #URL示例：https://restapi.amap.com/v3/traffic/status/road?name=北环大道&adcode=440300&key=<用户的key>
        url = AMAP_TRAFFIC_DATA_BASE_URL + 'road'
        url = url + '?name=' + params['name'] + '&adcode=' + params['adcode'] + '&key=' + AMAP_WEB_API_KEY

        print('指定线路交通态势，url:' + url)

        data = ''
        with request.urlopen(url) as f:
            data = f.read()
            data = data.decode('utf-8')
            print('指定线路交通态势，高德返回数据:' + data)

        return {
            'code': '0',
            'msg': '成功！',
            'data': data
        }
    else:
        return {
            'code' : '1',
            'msg' : '传入范围类型不对！',
            'data' : {

            }
        }


#矩形
rectangle_params = {
    'rectangle' : '116.351147,39.966309;116.357134,39.968727'
}

#圆形
circle_params = {
    'location' : '116.3057764,39.98641364',
    'radius' : '1500'
}

#指定线路交通态势
road_params = {
    'name' : '北环大道',
    'adcode' : '440300'
}

#data = getTrafficData('rectangle', rectangle_params)

#data = getTrafficData('circle', circle_params)

#data = getTrafficData('road', road_params)

#print(data)


