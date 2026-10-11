1. Problem

Merge two sorted linked lists into one sorted linked list
2. Approach

I did not come up with it myself.
How it works.
    1. If list1 or list2 are None we will simply return the other list
    2. We will solve it recursively and basically, each function should pick the smallest of the two nodes list1 or list2(lets say list1) and set its pointer to the result of another recursive function call with list1.next and list2 as arguments
    3. Eventually, after all the function calls two lists would merge

3. Time Complexity

Time complexity is O(n + m), for n,m - sizes of list1 and list2
Each recursive function call we decrease one list by one element,
each time we will have to call the function recursively for every element in both arrays, unless initially list1 or list2 is none, then O(1)
5. Reflection / Improvement

Answer briefly:

    Recursive solution wouldn't work for large linked lists in Python, because the language has a limit of 1000 recursive function calls.
    It would be better to merge two linked lists iteratively

