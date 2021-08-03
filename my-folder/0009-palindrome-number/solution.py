class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum=0
        n=x
        while(x>0):
            rem = x%10
            sum = sum*10+rem
            #print(sum)
            x=x//10
        if sum==n:
            return True
        else:
            return False
        
