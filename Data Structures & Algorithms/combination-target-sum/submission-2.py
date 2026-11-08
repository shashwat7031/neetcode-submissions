class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i,total):
            if total > target or i == len(nums):
                return
            if total == target:
                if curr not in res:
                    res.append(curr.copy())
            curr.append(nums[i])
            backtrack(i,total+nums[i])
            curr.pop()
            backtrack(i+1,total)
        backtrack(0,0)
        return res
        