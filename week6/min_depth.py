class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        if (root.left is None) ^ (root.right is None):
            if root.left:
                return 1 + self.minDepth(root.left)

            else:
                return 1 + self.minDepth(root.right)


        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))