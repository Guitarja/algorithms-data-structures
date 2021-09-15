# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # https://leetcode.com/problems/binary-tree-coloring-game/discuss/350570/JavaC%2B%2BPython-Simple-recursion-and-Follow-Up
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        c = [0, 0]
        def count(node):
            if not node: return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        print(count(root))
        return count(root) / 2 < max(max(c), n - sum(c) - 1)