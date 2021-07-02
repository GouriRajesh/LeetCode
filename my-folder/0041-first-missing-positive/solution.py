class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count=0
        nums=set(nums)
        
        for item in nums:
            if item<0:
                count+=1

        if(count==len(nums)):        
            return 1
        else:
            t=1
            while(1):
                if t not in nums:
                    return t
                else:
                    t+=1       
        
        
