class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict = {}
        for i in nums:
            my_dict[i] = my_dict.get(i,0) +1
        res = []
        x = len(nums)/3
        for key,values in my_dict.items():
            if values > x:
                res.append(key)
        return res