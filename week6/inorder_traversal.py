class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        self.traverse(root, res)
        return res
    def traverse(self, root, res):
        if root:
            self.traverse(root.left, res)
            res.append(root.val)
            self.traverse(root.right, res)