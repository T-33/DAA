class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        depths = []
        self.traverse(root, depths, 0)
        return max(depths)

    def traverse(self, root, depths, depth):
        if root:
            self.traverse(root.left, depths, depth + 1)
            self.traverse(root.right, depths, depth + 1)
        depths.append(depth)