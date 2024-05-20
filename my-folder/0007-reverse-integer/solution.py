import sys
class Solution:
    def reverse(self, x: int) -> int:
        number = 0
        x1 = x
        n = x
        if(x<0):
            x = abs(x)
        while(x>0):
            rem = x%10
            if abs((number * 10) + rem) < 2**31 and ((number * 10) + rem) != 2**31 - 1:
                number = (number * 10) + rem
                x=x//10
            else:
                return 0
            
        if(n<0):
            return -abs(number)
        else:
            return number
        
