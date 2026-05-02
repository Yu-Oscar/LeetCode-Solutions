class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for i in range(len(strs)):
            key = (''.join(sorted(strs[i])))
            dictionary[key].append(strs[i])
        return [dictionary[value] for value in dictionary]