"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dfs= [head]
        dummy = Node(None, None, None, None)
        ans = dummy
        
        while dfs:
            node = dfs.pop()
            dummy.next = node
            if node.next:
                dfs.append(node.next)
            if node.child:
                dfs.append(node.child)
            node.child = None
            node.prev = dummy
            dummy = dummy.next
        
        ans = ans.next
        ans.prev = None
        return ans