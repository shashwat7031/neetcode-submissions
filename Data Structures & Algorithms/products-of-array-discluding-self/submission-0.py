class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        main_list = []
        for i in nums:
            index = nums.index(i)
            x = nums[index+1:]  
            y = nums[:index]   
            new_list = x + y       
            main_list.append(new_list)
        result = [] 
        for j in main_list:
            r = 1
            for k in j:
                r = r * k
            result.append(r)  

        return(result)