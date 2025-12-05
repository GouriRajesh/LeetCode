class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Idea: Consider each char as the center and expand around it. Edge is when it is even number of char in the string

        if not s:
            return

        max_length = 0
        max_palindrome = ""

        for i in range(len(s)):
            # Odd string
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    max_length = r - l + 1
                    max_palindrome = s[l : r + 1]
                l -= 1
                r += 1

            # Even string
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    max_length = r - l + 1
                    max_palindrome = s[l : r + 1]
                l -= 1
                r += 1

        return max_palindrome

