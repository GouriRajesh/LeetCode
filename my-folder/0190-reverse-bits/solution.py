class Solution:
    def reverseBits(self, n: int) -> int:
        binary_number = "{:032b}".format(n)
        res = ''
        for i in binary_number[::-1]:
            res+=i
        return int(res,2)
        
