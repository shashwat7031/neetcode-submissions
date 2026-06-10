class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)  # Convert nums to a set to remove duplicates
        nums_sorted = sorted(nums_set)  # Sort the unique numbers
        
        max_length = 1  # Initialize max length of consecutive sequence
        current_length = 1  # Initialize current length of consecutive sequence
        
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i - 1] + 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        # Final check to update max_length if the last sequence was the longest
        max_length = max(max_length, current_length)
        
        return max_length
