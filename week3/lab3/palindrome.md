1. Problem

Determine whether a linked list is a palindrome
2. Approach

- Create a list for nodes of the linked list
- Loop through the linked list, and add its values into an array
- Create two pointer on tails of the array: start, end = 0, len(arr) - 1
- Push those pointers to the middle, and at each step check if values are equal
- If values differ, return False, because list would not be a palindrome
- Otherwise return True
3. Time Complexity

Time Complexity: O(n)

We loop through the list and add its values into an array

4. Reflection / Improvement

There is an optimal solution that uses O(1) space, and it uses very interesting techniques.
Turns out we can find the middle of the linked list by using fast and slow pointers.
Because the fast pointer is twice faster than the slow pointer,
when fast pointer reaches the end, the slow pointer would precisely in the middle
We can then reverse the second half, and trace through both halves with two pointers

You do not have to implement the improved solution unless you want to.