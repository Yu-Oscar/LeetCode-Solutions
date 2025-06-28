class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apples = sum(apple)

        for i, size in enumerate(capacity):
            apples -= size
            if apples <= 0:
                return i + 1