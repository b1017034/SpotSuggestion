import urllib.request, json
import urllib.parse

import datetime

base_url = 'https://maps.googleapis.com/maps/api/directions/json?'
API_key = 'AIzaSyAHbEO8wQ-oUH55RtzlnUsb2ozb5BYC9kk'
a = 'waypoints=optimize:true|Barossa+Valley,SA|Clare,SA|Connawarra,SA|McLaren+Vale,SA'

def route(origin, destination, dep_time):
    unix_time = to_unix_time(dep_time, hours=9)

    parameters = 'language=ja&origin={}&destination={}&departure_time={}&key={}'.format(origin, destination, unix_time, API_key)
    parameters = urllib.parse.quote_plus(parameters, safe='=&')
    request = base_url + parameters

    # Google Maps Platform Directions APIを実行
    response = urllib.request.urlopen(request).read()

    # 結果(JSON)を取得
    directions = json.loads(response)

    #print(directions)

    print('出発地 -> 目的地')
    print(origin)
    print(destination)

    #所要時間を取得
    for key in directions['routes']:
        #print(key) # titleのみ参照
        #print(key['legs'])
        for key2 in key['legs']:
            print('')
            for key3 in key2['steps']:
                print('=====')
                print(key3['distance']['text'])
                print(key3['end_location']['lat'], key3['end_location']['lng'])
                print('=====')
            print('=====')
            print(key2['distance']['text'])
            print(key2['duration_in_traffic']['text'])
            print('=====')

def get_routes(origin, destination, dep_time, waypoint_array):
    unix_time = to_unix_time(dep_time, hours=9)

    waypoints = ''

    for waypoint in waypoint_array:
        waypoints += '|'+waypoint

    parameters = 'language=ja&origin={}&destination={}&departure_time={}&waypoints=optimize:true{}&key={}'.format(origin, destination, unix_time, waypoints, API_key)
    parameters = urllib.parse.quote_plus(parameters, safe='=&')
    request = base_url + parameters

    # Google Maps Platform Directions APIを実行
    response = urllib.request.urlopen(request).read()

    # 結果(JSON)を取得
    directions = json.loads(response)

    # 所要時間を取得
    for key in directions['routes']:
        # print(key) # titleのみ参照
        # print(key['legs'])
        for key2 in key['legs']:
            print(key2['start_address'])
            for key3 in key2['steps']:
                print('=====')
                print(key3['distance']['text'])
                print(key3['end_location']['lat'], key3['end_location']['lng'])
                print('=====')
            print('=====')
            print(key2['end_address'])
            print('=====')


def to_unix_time(time, hours=0):

    #UNIX時間の算出
    dtime = datetime.datetime.strptime(time, '%Y/%m/%d %H:%M')
    dtime = dtime + datetime.timedelta(hours=hours)
    unix_time = int(dtime.timestamp())
    return unix_time
