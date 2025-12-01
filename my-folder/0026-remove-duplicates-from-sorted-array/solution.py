class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Length of array
        n = len(nums)
        # Start with first element -> always unique
        i = 0
        # Initialize element to compare to
        element = nums[i]
        # Start loop from second element till end of array
        j = 1
        while j < n:
            # If number is same as the element -> Move ahead
            if nums[j] == element:
                j += 1
            # If number is not same as the element, is unique
            else:
                # Update element
                element = nums[j]
                # Set next value of current index to be the new element
                nums[i + 1] = nums[j]
                # Move index forward
                i += 1

        # Current index + 1 -> Gives the count of unique elements found
        return i + 1

