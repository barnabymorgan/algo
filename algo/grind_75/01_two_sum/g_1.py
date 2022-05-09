class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = dict()
        pos = 0
        
        while pos < len(nums):
            if (target - nums[pos]) not in dictionary:
                dictionary[nums[pos]] = pos
                pos += 1
            else:
                return [dictionary[target - nums[pos]], pos]
        
#        for i in range(0, len(nums)):
#            for j in range(i+1, len(nums)):
#                i_value = nums[i]
#                j_value = nums[j]
#                
#                if i_value + j_value == target:
#                    return [i, j]
