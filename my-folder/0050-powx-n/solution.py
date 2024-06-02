class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
            return Solution.myPow(self, x, n)
        elif n == 0:
            return 1.0
        else:
            half = Solution.myPow(self, x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
    
        
