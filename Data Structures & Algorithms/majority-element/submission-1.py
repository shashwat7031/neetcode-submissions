class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dic = {}
        for i in nums:
            my_dic[i] = my_dic.get(i,0)+1
        v = 0
        k = 0
        for key,val in my_dic.items():
            if val>v:
                k = key
                v = val
        return k