class Solution:
    def addDigits(self, num: int) -> int:
        #original number is divisible by 9 if and only the sum of its digits is also divisible by 9
        if num == 0 :
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


        