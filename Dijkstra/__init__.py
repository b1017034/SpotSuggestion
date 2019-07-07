import Dijkstra.DijkstraNode

class SpotDijkstra():
    def __init__(self, DijkstraNode):
        self.root = DijkstraNode
        self.DijkstraNode = DijkstraNode

    def add_node(self, DijkstraNode, edge):
        if self.root:
            self.root.add_node(DijkstraNode, edge)
        else:
            self.root = DijkstraNode

    def find(self, node_id):
        if self.root:
            return self.root.find(node_id)

    def find_add_node(self, DijkstraNode, edge, node_id):
        if self.root:
            self.root.find_add_node(DijkstraNode, edge, node_id)

    def routes(self, node_id, values=None):
        if self.root:
            values =self.root.routes(node_id, values=values)

        return values

    def routes_test(self, node_id):
        if self.root:
            self.root.routes_test(node_id)