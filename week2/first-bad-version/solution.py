class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        middle = (left + right) // 2
        while left != right:
            print(left, right, middle)
            if isBadVersion(middle):
                right =  middle
            else:
                left = middle + 1
            middle = (left + right) // 2
        return middle
