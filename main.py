from BinarySearchTree import BinarySearchTree
from BinarySearchTree.BinarySearchNode import BinarySearchNode
from Dijkstra import SpotDijkstra
from Dijkstra.DijkstraNode import DijkstraNode


def blt_test():
    root = BinarySearchTree(BinarySearchNode)

    root.insert(value=1)
    root.insert(value=2)
    root.insert(value=100)
    root.insert(value=2)
    root.insert(value=5)

    print(root.list())

def list_swap(node_list):
    nodes = []
    for one in node_list:
        nodes.append(DijkstraNode(40, one))
    for node in nodes:
        for added_node in nodes:
            node.add_node(added_node, 2)
    root = SpotDijkstra(nodes[0])
    return root

def dijkstra_test():
    node_list = [1,2,3,4,5]
    node_staytimes = [20,30,20,10,4]
    node_edges = [10,0,11,11,1]

    root = list_swap(node_list)

    lists = root.routes(2)
    print("=-----------=")
    for list in lists:
        print(list)

dijkstra_test()