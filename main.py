from BinarySearchTree import BinarySearchTree
from BinarySearchTree.BinarySearchNode import BinarySearchNode
from Dijkstra import SpotDijkstra
from Dijkstra.DijkstraNode import DijkstraNode
from DataClasses.SpotDataClass import Spot

import json
import numpy as np
from flask import Flask, request



def blt_test():
    root = BinarySearchTree(BinarySearchNode)

    root.insert(value=1)
    root.insert(value=2)
    root.insert(value=100)
    root.insert(value=2)
    root.insert(value=5)

    print(root.list())


def list_swap(spots):
    nodes = []
    for index in range(len(spots)):
        nodes.append(DijkstraNode(spots[index].stay_time, index))
    for node in nodes:
        for added_node in nodes:
            node.add_node(added_node, 2)
    root = SpotDijkstra(nodes[0])
    return root


def create_spots():
    spot_list: list[list[str, float, float]] = [["公立はこだて未来大学", 41.8332672, 140.7606784],
                                                ["五稜郭タワー", 41.8104462, 140.7445977],
                                                ["五稜郭駅", 41.8108967, 140.7463324],
                                                ["函館山", 41.7669551, 140.7175339],
                                                ["木古内駅", 41.6700811, 140.4524394]]
    spots: list[Spot] = []
    for spot in spot_list:
        spots.append(Spot(spot[0], spot[1], spot[2], 40))
    return spots


def calc_route(routes, spots):
    required_time = []
    for _, route in enumerate(routes):
        sum = 0
        for index_, id in enumerate(route):
            if id < len(spots) and index_ < len(route) - 1:
                sum += spots[id].difference(spots[route[index_ + 1]])
            if index_ == 5:
                print(sum)
        required_time.append(sum)
    return required_time

def max_index(required_time, n):
    time_np = np.array(required_time)
    # ソートはされていない上位k件のインデックス
    unsorted_max_indices = np.argpartition(-time_np, n)[:n]
    # 上位k件の値
    y = time_np[unsorted_max_indices]
    # 大きい順にソートし、インデックスを取得
    indices = np.argsort(-y)
    # 類似度上位k件のインデックス
    return unsorted_max_indices[indices]


def min_index(required_time, n):
    time_np = np.array(required_time)
    # ソートはされていない上位k件のインデックス
    unsorted_max_indices = np.argpartition(time_np, n)[:n]
    # 上位k件の値
    y = time_np[unsorted_max_indices]
    # 大きい順にソートし、インデックスを取得
    indices = np.argsort(y)
    # 類似度上位k件のインデックス
    return unsorted_max_indices[indices]


def get_route(spots, routes):
    required_time = calc_route(routes, spots)

    max_list = min_index(required_time, 4)

    for index in max_list:
        for id in routes[index]:
            print(spots[id].name)
        print("距離は" + str(required_time[index] / 1000) + "km")
    print("=-----------=")


def dijkstra_test():
    spots = create_spots()
    root = list_swap(spots)

    routes = root.routes(2)

    get_route(spots, routes)


"dijkstra_test()"

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    print(request.data.decode())
    return "Hello World!"


app.run(host="localhost", port=5000)