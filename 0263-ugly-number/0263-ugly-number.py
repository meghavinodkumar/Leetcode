class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0 :
            return False
        def divisibility(dividend, divisor):
            while dividend % divisor == 0:
                dividend //= divisor 
            return dividend
        primeList = [2,3,5]
        for factor in primeList:
            n = divisibility(n,factor)
        return n == 1
        