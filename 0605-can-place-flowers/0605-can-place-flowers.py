class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0 
        flowerBedLength = len(flowerbed)
        for i in range(flowerBedLength):
            #condition to check if the current plot is empty
            if flowerbed[i] == 0:
                #since the current plot is empty, checking if the left and right plots adjacent to it are empty as well 
                leftEmptyPlot = (i == 0) or (flowerbed[i-1] ==0)
                rightEmptyPlot = (i == flowerBedLength - 1) or (flowerbed[i+1] == 0)
                #We can plant a flower if both of the plots are empty 
                if leftEmptyPlot and rightEmptyPlot :
                    flowerbed[i] = 1
                    count += 1
        return count >= n


        