class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Length of nums
        n = len(nums)
        # Start with second elements for cleaner loop
        low = 1
        # Start with second last element for cleaner loop
        high = n - 2

        # When length is only 1
        if n == 1:
            return nums[0]
        # When 1st and 2nd element are not equal
        if nums[0] != nums[1]:
            return nums[0]
        # When last and 2nd last element are not equal
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        while low <= high:
            mid = (low + high) // 2
            # Stopping condition when mid is not equal to either left or right value
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # Standing on odd index and prev is equal or standing on even index and next is equal -> Left is equivalent -> element is on right
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (
                mid % 2 == 0 and nums[mid] == nums[mid + 1]
            ):
                low = mid + 1
            # Right is equivalent -> element is on left
            else:
                high = mid - 1

        return -1

