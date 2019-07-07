class BinarySearch:
    def __init__(self, nodeDataClass):
        self.root = None
        self.nodeDataClass = nodeDataClass

    # Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data['index'] < self.data['index']:
                if self.left is None:
                    self.left = NodeDataClass.Node(data)
                else:
                    self.left.insert(data)
            elif data['index'] > self.data['index']:
                if self.right is None:
                    self.right = NodeDataClass.Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

        # findval method to compare the value with nodes

    def findval(self, lkpval):
        if lkpval < self.data['index']:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.search(lkpval)
        elif lkpval > self.data['index']:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.search(lkpval)
        else:
            print(str(self.data) + ' is found')

        # Print the tree

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
