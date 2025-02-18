class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        counter1=0
        counter2=1
        for counter2 in range(len(nums)):
            #if my element at the current index is non zero then swap it with the one in the previous index 
            if nums[counter2]!=0:
                nums[counter2],nums[counter1]=nums[counter1],nums[counter2]
                counter1+=1
        return nums
        



        

        