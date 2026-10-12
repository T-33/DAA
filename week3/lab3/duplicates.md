1. Problem

Remove duplicates in a sorted linked lists. Keep one of each value
2. Approach

    I have two pointers prev and current
    - If they have the same value, I would move pointer of prev over the current, so set it prev.next = curr.next
    - If they dont have the value, I would just move them one element forward each
    - I will continue doing it, until curr==None
    - Then i can return the head
3. Time Complexity

Time Complexity: O(n)
We always loop through the whole list

4. Reflection / Improvement

It is the optimal solution.
I had a problem with code style and some code that could have been deleted, overall algorithm was the same, I later refactored with AI
