class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute-Force Solution
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # Hap-Map Solution
        nums_map = {}
        # Iterate over all numbers in the list
        for i in range(len(nums)):
            # Find the complement of current number
            complement = target - nums[i]
            # If index of complement is already known through hash-map -> return it
            if complement in nums_map:
                return [i, nums_map[complement]]
            # Else add current element to the hah-map with index
            nums_map[nums[i]] = i

