"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root):	
        serial = []

        def preorder(node):

            if not node:
                return

            serial.append(str(node.val))

            for child in node.children:
                preorder(child)

            serial.append("#")      # indicates no more children, continue serialization from parent

        preorder(root)
        # print(",".join(serial))
        return ",".join(serial)

    def deserialize(self, data):	
        if not data:
            return None

        tokens = deque(data.split(","))
        root = Node(int(tokens.popleft()), [])

        def helper(node):

            if not tokens:
                return

            while tokens[0] != "#": # add child nodes with subtrees
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)

            tokens.popleft()        # discard the "#"

        helper(root)
        return root

#Serialize with preorder traversal where sentinel "#" indicates the final child of a node has been processed, so the function returns to its parent call.
# Deserialize by creating a deque (could also use an iterator with next() instead of popleft()).
# While the next item is not "#", create a child with the item, add the child to the list of children and recurse to create its subtree.
# Repeat until there are no more children, then ignore the "#".

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
