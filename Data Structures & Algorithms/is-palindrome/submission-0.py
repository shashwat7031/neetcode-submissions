class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for i in range(len(s)):
            if s[i].isalnum():
                x += s[i].lower()
        l = 0
        r = len(x) - 1
        while l <=r:
            if x[l] == x[r]:
                l +=1
                r -=1
            else:
                return False
        return True
            