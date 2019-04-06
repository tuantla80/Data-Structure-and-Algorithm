class BinaryTree(object):

    def __init__(self, root):
        self.root = root  # sometimes we call root as a key
        self.left_child = None  # left child of the root
        self.right_child = None  # right child of the root

    def insert_left(self, new_node):
        if self.left_child == None:  # No left child so adding it to the tree
            self.left_child = BinaryTree(new_node)
        else:  # having left child
            sub_tree = BinaryTree(new_node)
            sub_tree.left_child = self.left_child  # push existing child down 1 level to the tree at left
            self.left_child = sub_tree

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            sub_tree = BinaryTree(new_node)
            sub_tree.right_child = self.right_child  # push existing child down 1 level to the tree at right
            self.right_child = sub_tree

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_value(self):
        return self.root

    def set_root_value(self, v):
        self.root = v


if __name__ == "__main__":
    r = BinaryTree(root='ROOT')
    print("root value = {}".format(r.get_root_value()))

    r.insert_left('LEFT')
    print("left child = {}".format(r.get_left_child()))  # <__main__.BinaryTree object at 0x00000251DAF4CD30>
    print("left child = {}".format(r.get_left_child().get_root_value()))  
