1. Problem

Detect if the tail node of a linked list points to another node in the list.
2. Approach

    1. Create a set of nodes we have visited
    2. If we already have visited current node, return True, that means a cycle
    3. recursively run the same algorithm for the rest of the list
3. Time Complexity

In the worst case, the tail will be pointing to itself, and we would have traversed the whole list,
 thus making it 
 
 O(n)

If I have used a list instead of a set, time complexity would have been O(n^2), because checking if an element is in an array is O(K)

5. Reflection / Improvement

There is no more efficient approach time wise, O(n) is optimal, however there is O(1) space complexity solution
called Floyd's algorithm or tortoise and hare algorithms, basically what we would do:
    1. setup two pointers 1 - current node, 2- node after the next
    2. If there is no node after the next, there is no cycle
    3. While there is node after the next, we will jump those two pointers 1 node and 2 nodes ahead respectively.
    4. If there is a cycle the fast pointer will catch up the slow and that would mean there is a cycle

You do not have to implement the improved solution unless you want to.