class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_values(num):
            return int(''.join(str(mapping[int(digit)]) for digit in str(num)))
        return sorted(nums, key=map_values)
        
        