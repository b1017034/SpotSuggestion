import dataclasses


@dataclasses.dataclass()
class BinarySearchNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # search value in node
    def search(self, data):
        if data < self.data:
            if self.left is None:
                return str(data) + " Not Found"
            return self.left.search(data)
        elif data > self.data:
            if self.right is None:
                return str(data) + " Not Found"
            return self.right.search(data)
        else:
            print(str(self.data) + ' is found')

    def delete_left(self, data):
        if data < self.data:
            if self.left:
                self.left.delete_left(data)
                promoted = self
            else:
                print(str(data) + "is not found")
        elif data == self.data:
            if self.left:
                promoted = self.left._search_max()
                promoted.left = self.left._delete_max()
                promoted.right = self.right
            else:
                promoted = self.right
        elif self.data < self.data:
            if self.right:
                self.right = self.right.delete_left(data)
                promoted = self
            else:
                print(str(data) + "is not found")
        return promoted

    def list(self):
        left = self.left.list() if self.left else []
        center = [self.data]
        right = self.right.list() if self.right else []
        return left + center + right

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.data
        if self.right:
            yield from self.right

    def _search_max(self):
        if self.right:
            return self.right._search_max()
        else:
            return self

    def _delete_max(self):
        if self.right:
            self.right = self.right._delete_max()
            promoted = self
        else:
            promoted = self.left
        return promoted


    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
