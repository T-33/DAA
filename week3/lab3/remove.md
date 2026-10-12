1. Problem

Given a val, remove the nodes from the linked list with that val
2. Approach

- Basically, I loop thorugh linked list and if the node's value next to the pointer is specified val, I set curr.next to curr.next.next,
thus deleting the node
- There is an important edge case, if head of the list should be deleted, the above algorithm would fail, because it only checks for curr.next's value, it works completely fine for nodes in the middle and at the end.
- To fix it, we would simply turn the first node into the second one, by creating a dummy node and pointing it to the head
- Then we would return the node dummy is pointing to
3. Time Complexity

Time Complexity: O(n)

In the worst case, value that should be deleted, would be at the tail. We would have to loop thorugh the whole list

4. Reflection / Improvement

My solution is optimal.
I really like the dummy technique
You do not have to implement the improved solution unless you want to.