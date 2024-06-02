class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1,-1]
        elif len(nums) == 1 and nums[0] == target:
            return [0,0]
        else:
            first = nums.index(target) if target in nums else -1
            last = -1
            if(first != -1):
                nums.sort(reverse = True)
                last = len(nums) - 1 - nums.index(target)
            return [first, last]

