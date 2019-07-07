class BinarySearchTree:
    def __init__(self, BinarySearchNode):
        self.root = None
        self.BinarySearchNode = BinarySearchNode

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = self.BinarySearchNode(value)

    def search(self, value):
        if self.root:
            self.root.search(value)
        else:
            print("BinarySearchNode is not initialized")

    def list(self):
        if self.root:
            return self.root.list()
        else:
            print("BinarySearchNode is not initialized")
            return []

    def delete_left(self, value):
        if self.root:
            self.root.delete_left(value)
        else:
            print("BinarySearchNode is not initialized")
            raise ValueError