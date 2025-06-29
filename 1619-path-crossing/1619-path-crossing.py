class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = [0,0]
        direction = {'N':[0,1], 'E':[1,0], 'W':[-1,0], 'S':[0,-1]}
        visited = set()
        visited.add(tuple(pos))


        for move in path:
            pos[0] += direction[move][0]
            pos[1] += direction[move][1]

            if tuple(pos) in visited:
                return True

            visited.add(tuple(pos))
        
        return False

        