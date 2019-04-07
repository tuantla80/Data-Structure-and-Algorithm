class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


import collections

def print_level_order_of_tree(tree):
    if not tree:
        return
    nodes = collections.deque([tree])  # using deque buitin function in Python
    current_count = 1  # run from the root
    next_count = 0

    while len(nodes) != 0:
        current_node = nodes.popleft()  # A deque: can pop left (popleft() function or pop right (pop() function
        current_count -= 1
        print(current_node.val)
        if current_node.left:
            nodes.append(current_node.left)
            next_count += 1
        if current_node.right:
            nodes.append(current_node.right)
            next_count += 1
        if current_count == 0:
            print('\n')
            # swap 2 variable using Python way.  a,b = b,a
            current_count, next_count = next_count, current_count


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    print_level_order_of_tree(root)
