## 1. Problem
Given an array of number 1, 2, ..., n that represent versions of some software, starting from some 
buggy version k, every version from from k to n is also buggy, we need to find the first buggy version
## 2. Approach

	1) Similarly to binary search I create 3 variables: left, right and middle. Left initially is set to 0, and 		right=n, middle is the middle number between left and right
	2) We start a while loop that will terminate where left will be equal to right, i.e. we will have found the 	first buggy version
	3) In the loop we check if middle is a bad version
	4) If it is the bad version then either the middle is the first bad version or first bad version if smaller that middle, thats why we set right=middle
	5) If middle is the good version then the first bad version is greater than middle, so we set left=middle+1(we did not set right=middle+1 in case that middle is the first bad version)
	6) Update middle
	7) We repeat steps 2 through 6 until left=right, meaning we have an array of 1 element, that would be the first buggy version

## 3. Time Complexity
We will calculate time complexity similarly to binary search.
In the worst case, we will be finding the first buggy version at the last possible moment
Each iteration will be cutting the search area in half. Lets use the tracing method to calculate time complexity
Given: k - number of iterations, n - search area
k	n
0	n
1	n/2
2	n/4 = n/(2^2)
3	n/8 = n/(2^3)
k	n/(2^k)

We will only finish searching when n=1
n/(2^k) = 1 (multiply both sides by 2^k)
n = 2^k (take log2 of both sides)
log2 n = log2 2^k
log2n = k

Answer: Time complexity = O(log2n)

4. Space Complexity
We need only 3 variables: left, right and middle ------> space complexity is constant O(1)

5. Reflection / Improvement
	Binary search is the optimal algorithms for this problem, implementation-wise there is an important thing.
	Online most solutions calculate middle=left + (right-left)//2)
	I found that weird, because there is a clearer way to calculate middle= (left+right)//2
	Turned out that my way was not the best, because of integer overflow (That also applies to my binary search assignment)
	Given n < 2^31-1 = 2,147,483,647 
	If left and right will be close to this upper bound, lets say:
	left = 2000000, right = 2100000.
	Then calculating middle = (left + right)//2, left+right will be greater than 2^31-1, which in some 
	languages will overflow and result in a negative number or other error.
	The optimal way: middle = left + (right - left)//2 is better, because right-left will be within the integer upper bound (right > left)
