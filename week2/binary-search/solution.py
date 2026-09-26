class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle_idx = (right + left) // 2
        middle_number = nums[middle_idx]
        
        while True:
            if right - left == 1:
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                return -1
            if right - left == 0:
                if middle_number == target:
                    return middle_idx
                else:
                    return -1
            if target > middle_number:
                left = middle_idx + 1

            if target < middle_number:
                right = middle_idx
            if target == middle_number:
                return middle_idx
            middle_idx = (right + left) // 2
            middle_number = nums[middle_idx]

        return -1
