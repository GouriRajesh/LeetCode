class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # If same elements as k, take all
        if len(cardPoints) == k:
            return sum(cardPoints)

        n = len(cardPoints)
        # Take k elements from front initially for max sum
        curr_sum = sum(cardPoints[:k])
        # l points to kth elememt from front
        l = k - 1
        # r points to last element
        r = n - 1
        max_sum = curr_sum

        while l >= 0:
            # From current sum remove lth element from front and add rth element from back
            curr_sum = curr_sum - cardPoints[l] + cardPoints[r]

            # If greater than current sum update
            if curr_sum > max_sum:
                max_sum = curr_sum

            # Reduce l by 1 and r by 1
            l -= 1
            r -= 1

        return max_sum

