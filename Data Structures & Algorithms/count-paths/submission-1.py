class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        the_last_row = [1]*n
        for _ in range(m-1):
            for index in range(n-2,-1,-1):
                the_last_row[index] = the_last_row[index] + the_last_row[index+1]
        return the_last_row[0]