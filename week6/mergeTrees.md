# Problem
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.
## Solution
    * recursive base case * : if we have want to merge left subtree with empty right subtree, we simple return left subtree
    and vice versa
    - if we want to merge two subtrees, we return a new node, with its value = left.val + right.val, and left subtree set to
    mergeTrees(root1.left, root2.left)
    and right subtree set to 
    mergeTrees(root1.right, root2.right)
## Time Complexity
    O(min(N, M)) - because when one of the subtrees becomes None, we simply return the other
## Reflection-Improvement
 This is an optimal solution
