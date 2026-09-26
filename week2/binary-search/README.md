## 1. Problem
Given an array and target variable, find the index of the target variable in the array or return -1
## 2.Solution
I create 4 variables: left, right, middle_idx, middle_value.
Left starts out as 0 and right as the index of the last element of the array. 
	1) Middle_idx is calculated as the middle index between left and right, and middle_value is the value at array[middle_idx]. 
	2) Then we check if middle is equal to target, if it is then we return the middle idx. 
	3) If target is smaller than middle value then we shift variable right=middle_idx, thus halving the initial arrays size, then we repeat from step 1.
	4) We also need to perform a few checks in case of 1 and 2 sized arrays between left and right
## 3.Time complexity:
Suppose in the worst case scenario the target will be foundat the last possible moment, when array size is 2,
then my algorithm would check if left or right is target and return target index or -1.
Then each iteration left and right border would cut out the half of the array.
Let k be the number of iteration and n the size of the array in which we will be looking for target
k    n
1    n/2 = n/(2^1)
2    n/2 / 2 = n/4 = n/(2^2)
3    n/4 / 2 = n/8 = n/(2^3)
k    n/(2^k)

Our algorithm will end when array size n/(2^k) will be equal to 2
n/(2^k) = 2 (lets take log2 of both sides)
log2(n/(2^k)) = log2(2) we can factorize the left hand side using the formula for difference of logarithms

*log a - log b = log (a/b)*

log2 n - log2 (2^k) = 1
log2 n = log2 (2) + log2(2^k) = 1 + k
log2 n = 1 + k (we can omit the 1)
log2 n = k
Time complexity = O(log2 n)

## 4. Space complexity
At each iteration we need only 4 variables, hence we have O(1) constant space requirements

## 5. Reflections

I believe that log2 n is the best time complexity, however i dont have the ideal implementation, I saw implmeentations online and they dont need to check if left is equal to right and if left and right are right next to each other, because of while left <= right and at some point where array has only 1 element right shifts past left.

