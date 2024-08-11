class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = dict()
        for i, num in enumerate(nums):
            if target - num in map:
                prevIndex = map[target - num]
                return [prevIndex, i]
            map[num]= i
        return[-1,-1]
        
                
                