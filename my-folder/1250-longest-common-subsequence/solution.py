class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # If you want to print the LCS
        res_string = ""
        # DP: Recursion -> Memoization -> Tabulation
        n = len(text1)
        m = len(text2)
        # Step 0: Declare DP array
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        # Step 1: Update Base Cases -> Shifting of indices. 0 used to represent -1 index.
        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(m + 1):
            dp[0][j] = 0

        # Step 2: Loop for remaining cases
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Strings Match
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    res_string += text1[i - 1]
                # Strings Don't Match
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(res_string)
        return dp[n][m]

