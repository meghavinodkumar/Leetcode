class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, number in enumerate(nums):
            target_sum = target - number
            if target_sum in num_to_index :
                return [num_to_index[target_sum], index]
            num_to_index[number] = index
        return []

        
        