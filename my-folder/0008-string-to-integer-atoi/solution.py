class Solution:
    def myAtoi(self, s: str) -> int:
        res_string = ""
        sign = ""
        for c in s:
            if c == " " and res_string ==  "" and sign == "":
                continue
            elif (c == "+" or c == "-") and res_string ==  "" and sign == "":
                sign = c
            elif (c == "+" or c == "-") and sign != "":
                break
            elif c == "0" and res_string ==  "" and sign != "":
                continue
            elif c.isdigit():
                res_string = res_string + c
            else:
                break
        
        if(res_string != ""):
            result = int(res_string)
            if sign == "-":
                result = 0 - result
            if result < pow(-2,31):
                result = pow(-2,31)
            elif result > (pow(2,31) - 1):
                result = pow(2,31) - 1 
            return result
        else:
            return 0
