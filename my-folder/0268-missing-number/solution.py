class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n_sum = n*(n+1)//2
        res_sum = sum(nums)

        res = n_sum - res_sum

        return res 
        
        
