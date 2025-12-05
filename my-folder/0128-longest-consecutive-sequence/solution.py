class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use concept of: is this the start? by checking num -1 in list? -> if not, yes this is start and check in loop

        if not nums:
            return 0

        # Initialze
        nums_set = set(nums)  # To remove duplicates
        max_length = 0

        # Check all elements in the set
        for num in nums_set:
            length = 0
            # prev element present so skip checking this
            if num - 1 in nums_set:
                # Skip checking next consecutive as this is not the start and a lower prev element exists in the set -> Move to next
                continue
            # Not in the set -> this is the start so check consecutive elements
            else:
                ls = []
                next_num = num + 1
                length = 1

                while next_num in nums_set:
                    length += 1
                    ls.append(next_num)
                    next_num = next_num + 1

                if length >= max_length:
                    max_length = length
                    longest_sequence = []
                    longest_sequence.append(num)
                    for i in ls:
                        longest_sequence.append(i)

        print(longest_sequence)
        return max_length

