# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        paths = []
        self.dfs(root, paths, "")
        return paths

    def dfs(self, root, paths, curr_path):
        if not root:
            return
        if curr_path:
            curr_path += f"->{root.val}"
        else:
            curr_path = str(root.val)
        if root.left is None and root.right is None:
            paths.append(curr_path)
            return
        if root.left:
            self.dfs(root.left, paths, curr_path)
        if root.right:
            self.dfs(root.right, paths, curr_path)

