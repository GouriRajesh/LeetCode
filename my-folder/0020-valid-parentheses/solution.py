class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize stack
        stack = []
        # Traverse through entire string
        for char in s:
            # If opening bracket -> push to stack
            if char in ["(", "[", "{"]:
                stack.append(char)
            # If closing bracket -> pop from stack and compare
            if char in [")", "]", "}"]:
                # If stack is empty -> No matching opening bracket -> return False
                if len(stack) == 0:
                    return False
                # Pop element from stack and compare
                stack_element = stack.pop()
                if (
                    (char == ")" and stack_element != "(")
                    or (char == "]" and stack_element != "[")
                    or (char == "}" and stack_element != "{")
                ):
                    return False

        # Finally if stack is empty -> return True
        if len(stack) == 0:
            return True
        return False

