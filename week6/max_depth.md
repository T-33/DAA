# Problem
Calculate the maximum depth of a binary tree from the root to the leaf
## Solution
    1) create an empty array with depths of subtrees
    2) call a helper function dfs, with parameter depth that stores the depth reached so far
    3) DFS helper function calls itself on left and right subtree iteratively with depth + 1
    4) when DFS reaches bottom of the tree, it append depth to the depths array
    5) return max of depths array
## Time Complexity
O(N) - because we have to visit all nodes

## Reflection-Improvement
- It is time complexity optimal, however this problem can be solved with O(1) space complexity