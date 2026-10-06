class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in my_dict:
                return [my_dict[c],i]
            my_dict[nums[i]] = i
