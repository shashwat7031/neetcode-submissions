class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            condition = target - nums[i]
            
            if condition in pos:
                return [pos[condition], i]
            
            pos[nums[i]] = i