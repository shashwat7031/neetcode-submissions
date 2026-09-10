class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_dict = {}
        for i in nums:
            my_dict[i] = my_dict.get(i,0) + 1
        i = 0
        for key,value in my_dict.items():
            nums[i] = key
            i += 1
        return i