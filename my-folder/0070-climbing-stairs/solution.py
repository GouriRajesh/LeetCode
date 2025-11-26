class Solution:
    def climbStairs(self, n: int) -> int:
        # DP: Memoization
        # Step 0: Initialize DP array of size n+1
        dp = [-1] * (n + 1)

        def recurse(n):
            if n == 0 or n == 1:
                return 1
            # Step 2: Check if subproblem result exists in DP array, if yes return it, don't calculate again
            if dp[n] != -1:
                return dp[n]

            left_recursion_ways = recurse(n - 1)
            right_recursion_ways = recurse(n - 2)

            # Step 1: Store subproblem result in DP array
            dp[n] = left_recursion_ways + right_recursion_ways

            return dp[n]

        return recurse(n)

