1. Problem

Given a linked list of size n, return a sorted linked list in ascending order.
2. Approach

- We use the same general idea of Merge sort as with the array with a few implementation differences
- We find the middle of the linked list using fast and slow pointers. Because the fast pointer is twice faster than the slow,
when fast pointer reaches the end of the list, the slow pointer will be at the first node of the second half(if n is even), or exactly in the middle (if n is odd)
- Importantly, after finding the middle of the list, I run another loop  to find the node before the middle, to destroy the connection between two halves, or the algorithm will run in a loop
- Then we start two recursive subfunctions sortList on left and right halves, and return the result of a recursive helper function,
that zipper merges two linked lists

3. Time Complexity


Time Complexity: O(n logn)
Similarly to sorting the array, our function has the general form of:
T(n) = 2T(n/2) + n.

We will have log (n) recursive subcalls each will do O(n) work.
Resulting in
Time Complexity: O(n logn)

Then explain why.
4. Reflection / Improvement
There are a few implementation-wise improvemenets
- Implement helper merge function iteratively, to avoid max recursive subcalls limits
- There is no need to search the linked list the second time to find the element before the middle, we can find it the first slow, fast iteration
