class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter1=0
        counter2=0
        mergedString=""
        while ((counter1<len(word1)) and (counter2<len(word2))):
            mergedString+=word1[counter1]+word2[counter2]
            counter1+=1
            counter2+=1
        mergedString+=word1[counter1:]+word2[counter2:]
        return mergedString