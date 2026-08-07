class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            my_dict[i] = my_dict.get(i,0) +1
        
        return sorted(my_dict,key = lambda x:my_dict[x],reverse = True)[:k]
        
            