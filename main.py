from BinarySearchTree import BinarySearchTree
from BinarySearchTree.BinarySearchNode import BinarySearchNode
from Dijkstra import SpotDijkstra
from Dijkstra.DijkstraNode import DijkstraNode
from DataClasses.SpotDataClass import Spot

from GoogleMaps import Direction
from GoogleMaps import tsp

import json
import numpy as np
from flask import Flask, request

if __name__ == '__main__':
    waypoints = ['五稜郭タワー', 'ラッキーピエロ+美原店', 'ラーメン炙+五稜郭店']
    Direction.get_routes("五稜郭駅", "函館駅", "2019/10/25 12:00", waypoints)

