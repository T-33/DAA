1. Problem

Given an array of n elements, return an the same array sorted in ascending order.
2. Approach

I used a standard recursive merge sort.
- Base case: If array has 1 element or empty we return the array
- Then we create two variables: left and right
- We assign left and right to  be equal to the result of a recursive call of sortArray function with left and right halves of the initial array respectively
- Then we return the result of a helper function def merge, that zips two sorted arrays.
3. Time Complexity

Time Complexity: O(n*logn)
T(n) = 2T(n/2) + n.
We have logn subcalls that each merge two lists in O(n) resulting in total time complexity of
O(n*logn)

Then explain why.
4. Reflection / Improvement
- I believe this is an optimal solution.
- However there is a better implementation, that mergest two sorted lists iteratively.
- It is better because recursive stack is limited(1000 calls in python), and may be overflown on large lists