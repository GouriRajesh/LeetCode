class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both in increasing order
        g = sorted(g)
        s = sorted(s)
        # Counter for content children
        content = 0
        # Start from beginning till either children exist or cookies exist
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            # If content factor <= size of cookie -> Increase and move to next child
            if g[i] <= s[j]:
                content += 1
                i += 1
                j += 1
            # Try with next cookie
            else:
                j += 1
        # Return content children
        return content

