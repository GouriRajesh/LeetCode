class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Cleaning string
        new_s = []
        for i in s:
            if i.isalnum():
                new_s.append(i.lower())

        # Check if reverse is same
        return new_s == new_s[::-1]

