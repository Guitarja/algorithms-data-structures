# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def binary_search(root2, target2):
            if not root2:
                return False
            if root2.val == target2:
                return True
            elif root2.val > target2:
                return binary_search(root2.left, target2)
            else:
                return binary_search(root2.right, target2)
        
        def dfs(root, target):
            if not root:
                return False
            if binary_search(root2, target - root.val):
                return True
            return dfs(root.left, target) or dfs(root.right, target)
        
        return dfs(root1, target)
# time m*logn Let m, n be the number of nodes in the two trees.
# space logm + logn The space complexity of DFS over a binary tree is O(h), where hhh is the tree's height. This is because the DFS algorithm uses a call stack to keep track of the nodes it has visited, and the maximum size of the call stack is proportional to the height of the DFS tree. Assume that both trees are balanced, then the height of root1 and root2 is O(log⁡m) and O(log⁡n), respectively.