class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # if nums contains only +ve integers -> we can ALWAYS reach the end
        if 0 not in nums:
            return True

        # if nums contains 0 -> check further
        # Max index position we can reach
        maxPossiblePos = 0
        i = 0
        # Loop through nums
        while i < len(nums):
            # if we reached the last index or can reach beyond that -> break from loop
            if maxPossiblePos >= len(nums) - 1:
                break

            # if current index goes beyond max position we can reach -> break, cannot physically reach there
            if i > maxPossiblePos:
                return False

            # Update max index position we can reach = current index(i) + max jump possible at that index
            if (i + nums[i]) > maxPossiblePos:
                maxPossiblePos = i + nums[i]
                
            # Move to next index
            i += 1

        # If we reach here -> it means we can reach the last index
        return True

