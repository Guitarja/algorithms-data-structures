# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.res = 0
        self.helper(root)
        return self.res

    # lres and rres tells when left and right subtree are valid bst or not
    # if root is None, just return 0
    # lcount, rcount tell total nodes in left and right subtree if left/right is valid
    # if it is not a valid bst just return 0 so parent knows that it can't depend
    # on its children
    def helper(self, root):
        if root:
            lres, lcount, lLow, lUpp = self.helper(root.left)
            rres, rcount, rLow, rUpp = self.helper(root.right)

            if lres and rres and lUpp < root.val < rLow:
                self.res = max(self.res, lcount + rcount + 1)
                return True, lcount + rcount + 1, min(lLow, root.val), max(root.val, rUpp)
            else:
                return False, 0, min(lLow, root.val, rLow), max(lUpp, root.val, rUpp)            
        else:
            return True, 0, float('inf'), float('-inf')  # so that I can do this: lUpp < root.val < rLow

# time n
# space n