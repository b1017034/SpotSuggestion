import dataclasses

@dataclasses.dataclass()
class DijkstraNode:
    def __init__(self, stay_time, node_id):
        self.stay_time = stay_time
        self.id = node_id
        self.edge = []
        self.nodes = []
        self.is_done = False

    def add_node(self, DijkstraNode, edge):
        self.nodes.append(DijkstraNode)
        self.edge.append(edge)

    def find_add_node(self, DijkstraNode, edge, node_id):
        self.find(node_id).add_node(DijkstraNode, edge)

    def find(self, node_id, routes=[]):
        self.is_done = False
        routes.append(self.id)
        if self.id == node_id:
            return self
        for node in self.nodes:
            self.is_done = True
            if routes.count(self.id) == 0:
                node.find(node_id, routes)

        return DijkstraNode

    def routes(self, goal_id, routes=None, values=None):
        if routes is None:
            routes = []
        if values is None:
            values = []

        routes.append(self.id)
        if self.id is goal_id:
            "print(routes)"
            values.append(routes)
            return values

        for node in self.nodes:
            if routes.count(node.id) is 0:
                return_value = node.routes(goal_id, list(routes), values=values)
                if return_value is not None:
                    values = return_value
        return values

    def routes_test(self, goal_id, routes=None, values=[]):
        if routes is None:
            routes = []

        routes.append(self.id)
        if self.id is goal_id:
            print(routes)
            values.append(routes)
            return routes

        for node in self.nodes:
            if routes.count(node.id) is 0:
                node.routes_test(goal_id, list(routes))