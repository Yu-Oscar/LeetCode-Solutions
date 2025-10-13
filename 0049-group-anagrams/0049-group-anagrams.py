class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            curr = ''.join(sorted(s))
            if curr not in dic:
                dic[curr] = []
            dic[curr].append(s)

        return list(dic.values())