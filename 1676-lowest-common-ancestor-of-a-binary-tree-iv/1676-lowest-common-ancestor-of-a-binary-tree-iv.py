# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        def recu_LCA(root):
            if not root:
                return None
            if root in nodes:
                return root
            
            left, right = recu_LCA(root.left), recu_LCA(root.right)
            if left and right:
                return root
            return left or right
        
        return recu_LCA(root)
    
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/discuss/957784/Python-clean-recursive-solution-O(N)