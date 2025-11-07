class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set(nums)
        double_sum = sum(unique) * 2
        missing = double_sum - sum(nums)

        return missing
        
