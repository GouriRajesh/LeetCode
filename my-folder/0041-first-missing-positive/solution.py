class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        n=1
        while(True):
            if n not in nums:
                return n
            else:
                n+=1  
        
