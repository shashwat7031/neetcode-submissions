class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def capacity(start,end,gap):
            if(start > end):
                return end*gap
            else:
                return start*gap
        capacities = []
        n = len(heights)
        for i in range(n):
            for j in range(i + 1, n):  
                wa = capacity(heights[i], heights[j], j - i)
                capacities.append(wa)
        max_capacity = max(capacities) if capacities else 0
        return max_capacity