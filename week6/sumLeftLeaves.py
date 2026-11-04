# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None, left=False) -> int:
        if not root:
            return 0

        if root.left is None and root.right is None:
            if left:
                return root.val
            else:
                return 0
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)
