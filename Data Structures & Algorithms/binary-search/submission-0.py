class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            med = (left + right) // 2
            if target == nums[med]:
                return med
            elif target > nums[med]:
                left = med + 1
            else:
                right = med - 1
        
        return -1