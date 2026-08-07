class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        my_dic = {}
        result = []
        for i in nums:
            my_dic[i] = my_dic.get(i,0)+1
        small = min(my_dic)
        large = max(my_dic)
        for i in range(small,large+1):
            if i in my_dic:
                for j in range(my_dic[i]):
                    result.append(i)
        return result