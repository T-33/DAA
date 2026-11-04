# Problem
Calculate the minimum depth distance from root to leaf(min depth)
## Solution
    -*recursive base case*:
        - min depth of a single node is 1
        - min depth of an empty tree is 0
    - for a tree with two subtrees, the min depth would be 1 + min(minDepth(left), minDepth(right))
    - however we have to watch out for the case, when tree has only 1 child, then the algo would calculate min depth of None child as 0 and ignore the other subtree
    - to fix this we use a xor operator to determine if there is only one child,
        and then we return 1 + minDepth(existing_child)
## Time Complexity
O(N) - we visit all nodes
## Reflection-Improvement
- We can be doing much better in cases of degenerate trees, however depth first search would always teach the end of all nodes
- To fix this we can be doing breadth first search, that would stop when we hit the bottom of one of the subtreees
