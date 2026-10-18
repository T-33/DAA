class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if (n <= 1):
            return nums

        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        left_pointer = 0
        right_pointer = 0
        result = []

        while left_pointer < len(left) and right_pointer < len(right):
            left_val = left[left_pointer]
            right_val = right[right_pointer]
            if left_val < right_val:
                result.append(left_val)
                left_pointer += 1
            else:
                result.append(right_val)
                right_pointer += 1
        return result + left[left_pointer:] + right[right_pointer:]
