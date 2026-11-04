# Problem
Check if a given binary tree has a path from root to leaf, such that a sum of its nodes is equal to target

## Solution
    * recursive base case*
        - empty subtree can not have the target sum - returns False always
        - A single leaf has a valid sum only if target_sum == root.val
        - When we proceed the root, at least one of its subtrees shoudl have a target sum of target - root.val, for the algorithms to return True
## Time Complexity
O(N) - because we visit all nodes
## Reflection-Improvement
- Optimal solution