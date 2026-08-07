class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for i in strs:
            value = [0]*26
            for s in i:
                value[ord(s) - ord('a')] +=1
            my_dict[tuple(value)].append(i)
        return list(my_dict.values())