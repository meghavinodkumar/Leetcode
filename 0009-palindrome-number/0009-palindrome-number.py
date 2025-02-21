class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversedNumber=0
        original=x
        if x<0:
            return False
        while x>0:
            digit=x%10
            reversedNumber= reversedNumber*10+ digit
            x//=10
        return reversedNumber==original
            
        