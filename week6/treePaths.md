# Problem
Return an array of all root to leaf paths
## Solution
- create empty array paths that would hold all the subtree paths
- call helper function dfs on the tree root
- DFS helper function has curr_path and paths as arguments (curr_path holds the path so far)
- If dfs is visiting a leaf, it would append it to curr_path, and append curr_path to all paths
- otherwise it would append nodes value to curr_path and call dfs on subtrees
## Time Complexity
- O(N) - we visit all nodes
## Reflection-Improvement
- it is an optimal solution