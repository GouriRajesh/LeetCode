class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Two pointer and Sliding Window
        # TC: O(n)
        # SC: O(256)

        # Initialize
        max_length = 0
        longest_substring = ""
        char_index_map = {}
        n = len(s)
        l, r = 0, 0

        # Till you reach end of string
        while r < n:
            # See char for first time or char is behind current window
            if s[r] not in char_index_map or char_index_map[s[r]] < l:
                # Update character index in map
                char_index_map[s[r]] = r
                # Calculate new length
                length = r - l + 1
                # Update max length and longest substring if greater than current max
                if length >= max_length:
                    max_length = length
                    longest_substring = s[l : r + 1]
            # Saw character before in the same window
            else:
                # Move l to next place of same character seen before
                l = char_index_map[s[r]] + 1
                # Update character index in map to new index seen
                char_index_map[s[r]] = r
            # Move r by one
            r += 1
        # To return longest substring found
        print(longest_substring)

        return max_length

