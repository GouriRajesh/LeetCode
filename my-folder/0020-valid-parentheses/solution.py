class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if(ch=="(" or ch=="[" or ch=="{"):
                stack.append(ch)
            elif len(stack)==0:
                return False
            elif(ch==")"):
                if stack[len(stack)-1]=="(":
                    stack.pop()
                else:
                    return False
            elif(ch=="]"):
                if stack[len(stack)-1]=="[":
                    stack.pop()
                else:
                    return False
            elif(ch=="}"):
                if stack[len(stack)-1]=="{":
                    stack.pop()
                else:
                    return False
        
        if len(stack) ==0:
            return True
        else:
            return False

        
