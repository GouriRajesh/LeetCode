class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minimum = inf

        if len(nums) == 1:
            return nums[0]

        while low <= high:

            mid = (low + high) // 2
            if nums[low] == nums[high]:
                minimum = min(minimum, nums[low])
                low = low + 1
                high = high - 1
                continue

            # Left Sorted
            if nums[low] <= nums[mid]:
                minimum = min(minimum, nums[low])
                low = mid + 1  # Move to Right half
            # Right Sorted
            elif nums[mid] <= nums[high]:
                minimum = min(minimum, nums[mid])
                high = mid - 1  # Move to Left half

        return minimum

