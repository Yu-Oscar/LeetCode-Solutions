class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        for color, rod in re.findall(r'[A-Z]\d', rings):
            if rod not in rods:
                rods[rod] = set()
            rods[rod].add(color)
        
        ans = 0
        for rod in rods:
            if len(rods[rod]) == 3:
                ans += 1

        return ans
