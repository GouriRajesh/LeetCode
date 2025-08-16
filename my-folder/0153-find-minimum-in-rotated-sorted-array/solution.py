class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = inf

        while low <= high:
            mid = (low + high) // 2
            # Array already sorted or left and right parts are now sorted
            if nums[low] <= nums[high]:
                res = min(res, nums[low])
                break
            # Left sorted
            if nums[low] <= nums[mid]:
                res = min(res, nums[low])
                low = mid + 1  # Move to unsorted right to repeat
            # Right sorted
            else:
                res = min(res, nums[mid])
                high = mid - 1  # Move to unsorted left to repeat

        return res

