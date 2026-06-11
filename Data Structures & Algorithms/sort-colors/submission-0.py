class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        my_dic = {}
        result = []
        for i in nums:
            my_dic[i] = my_dic.get(i,0)+1
        for i in range(0,3):
            if i in my_dic:
                for j in range(my_dic[i]):
                    result.append(i)
        nums[:] = result[:]