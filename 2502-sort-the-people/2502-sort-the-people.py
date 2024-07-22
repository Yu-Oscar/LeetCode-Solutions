class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = zip(names, heights)
        zipped = sorted(zipped, key=lambda x: x[1], reverse = True)
        names, _ = zip(*zipped)
        return names