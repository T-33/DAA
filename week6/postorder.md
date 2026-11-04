# Problem
Traverse binary tree postorder and print a list of visited nodes

## Solution
1) we create an array res, that will store node values
2) we call helper  function dfs with the root of the tree, and pass res as an argument
3) in DFS function, if node is not None, we call dfs() for the left subtree,
then call dfs() on the right subtree, then append value of the current node to res
4) return res

## Time Complexity
O(N) - we visit all nodes
## Reflection-Improvement
- It is an optimal solution, however it can be done iteratively using a stack to emulate 
- recursive call stack
