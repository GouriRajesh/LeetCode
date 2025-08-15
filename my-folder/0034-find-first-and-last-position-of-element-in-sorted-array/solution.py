class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def first_pos(nums, n, target):
            low = 0
            high = n - 1
            first = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def last_pos(nums, n, target):
            low = 0
            high = n - 1
            last = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        first = first_pos(nums, n, target)
        if first == -1:
            return [-1, -1]
        else:
            last = last_pos(nums, n, target)
            return [first, last]

