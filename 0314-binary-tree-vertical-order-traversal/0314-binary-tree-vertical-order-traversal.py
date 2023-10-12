# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return 
        min_idx =  max_idx = 0
        res = collections.defaultdict(list)
        que = deque([(root, 0)])
        while que:
            node, idx = que.popleft()
            
            if node:
                res[idx].append(node.val)
                
                min_idx = min(min_idx, idx)
                max_idx = max(max_idx, idx)
                
                que.append((node.left, idx - 1))
                que.append((node.right, idx + 1))
        
        return [res[i] for i in range(min_idx, max_idx + 1)]
# time n, n  is the number of nodes in the tree.
# space n