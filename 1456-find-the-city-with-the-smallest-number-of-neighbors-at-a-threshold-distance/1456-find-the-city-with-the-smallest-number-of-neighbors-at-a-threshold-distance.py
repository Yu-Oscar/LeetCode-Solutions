class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for fromi, toi, weighti in edges:
            dist[fromi][toi] = weighti
            dist[toi][fromi] = weighti

        # Step 2: Apply Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Step 3: Count reachable cities
        min_reachable = float('inf')
        result_city = -1

        for i in range(n):
            reachable = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    reachable += 1
            # Step 4: Determine the result
            if reachable < min_reachable or (reachable == min_reachable and i > result_city):
                min_reachable = reachable
                result_city = i

        return result_city