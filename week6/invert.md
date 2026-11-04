# Problem
Invert a binary tree. Swap each left subtree of a every node with a right subtree
## Solution
    *recursion base case* - if root is None we return None;
    and if root has no children, then we return root
    
    - we call invertTree on the left subtree and right subtree
    - swap left and right subtree of the root
## Time Complexity
O(N) - because we have to visit all root
## Reflection-Improvement
1) It has optimal time complexity