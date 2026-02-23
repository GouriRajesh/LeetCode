class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # keep track of bills
        fives = 0
        tens = 0
        twentys = 0

        for bill in bills:
            # if 5 -> keep it
            if bill == 5:
                fives += 1
            # if 10 -> keep it + return 5
            elif bill == 10:
                tens += 1
                # if one 5 not available, return False
                if fives == 0:
                    return False
                else:
                    fives -= 1
            # if 20 -> keep it + return 10,5 or 5,5,5
            elif bill == 20:
                twentys += 1
                # if no 5 available (we need atleast one 5 for both cases) or 10 is 0 (cannot give 10,5) and three 5 not available (since cannot give 10,5 try to give 5,5,5) -> return False
                if (fives == 0) or (tens == 0 and fives < 3):
                    return False
                if tens > 0:
                    # Give back 10,5 (or)
                    tens -= 1
                    fives -= 1
                else:
                    # Give back 5,5,5
                    fives -= 3

        return True

