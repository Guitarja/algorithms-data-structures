# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            vali, low, high = stack.pop()
            if vali.val <= low or vali.val >= high:
                return False
            if vali.left:
                stack.append((vali.left, low, vali.val))
            if vali.right:
                stack.append((vali.right, vali.val, high))
        return True
    
# Complexity Analysis

# Time complexity : O(N)\mathcal{O}(N)O(N) in the worst case
# when the tree is BST or the "bad" element is a rightmost leaf.

# Space complexity : O(N)\mathcal{O}(N)O(N) to keep stack.