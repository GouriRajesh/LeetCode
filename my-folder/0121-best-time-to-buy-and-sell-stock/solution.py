class Solution:
    def maxProfit(self, prices: List[int]) -> int:

    
    
        mini = inf
        diff = 0

        for price in prices:
            if price<mini:
                mini=price
            else:
                diff = max(diff,price-mini)

        return diff
            
