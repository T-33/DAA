1. Problem

Two linked lists intercept at some point, find the first common node.
2. Approach

    - I declare a set for visited nodes of list1 (with the common part)
    - I loop through list1 and add all the nodes to the set 
    - Then I loop through the list2, and return the first node that is in the set of visited nodes.
    - IF there is no common node, return None
3. Time Complexity

Time Complexity: O(n)

In the worst case of lists having no intersection, or intersecting at the last node

4. Reflection / Improvement

There is a second approach that uses O(1) space and it is very clever.
The most obvious solution would have been to use two pointers and trace them through both arrays to the point of intersection.
That would not be possible because lists may have different length before intersection point.
There is a workaround to this problem, both pointers would trace list1 and list2
Pointer A would walk len(list1) + list(2)
Hence, pointers would eventually meet, on their second loop.
