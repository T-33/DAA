# Problem
Calculate the sum of all left leafs
## Solution
- We recursively traverse all the nodes
- If a given node is a leaf, and the parent passed the flag left=True, that means that node is a left leave
we return its value, otherwise it was a right leaf and we return 0
- then we return sum of leftLeaves for the left subtree (with left=True flag) + sum of leftLeaves of the right subtree
## Time Complexity
O(n) - because we visit every node
## Reflection-Improvement
This is an optimal solution, however there is a solution that doesnt require additional flag (left),
each root can check if its left subtree is a leaf and return the value of left leaf + sumLeftLeaves(right_subtree)