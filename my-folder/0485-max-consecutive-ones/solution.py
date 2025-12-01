class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            if i == 0:
                max_ones = max(max_ones, count)
                count = 0
                
        max_ones = max(max_ones, count)
        return max_ones

