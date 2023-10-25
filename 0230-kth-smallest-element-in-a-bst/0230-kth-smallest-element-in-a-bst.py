# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        def left_most(node):
            while node:
                stack.append(node)
                node = node.left

        def next():
            top = stack.pop()
            if top.right:
                left_most(top.right)
            return top.val

        left_most(node)
        for i in range(k):
            val = next()
        return val
