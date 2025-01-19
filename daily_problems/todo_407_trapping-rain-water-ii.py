class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m, n, ans = len(heightMap), len(heightMap[0]), 0
        vis = [[False] * n for _ in range(m)]
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heappush(pq, (heightMap[i][j], i, j))
                    vis[i][j] = True
        while pq:
            h, i, j = heappop(pq)
            for a, b in dirs:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and not vis[x][y]:
                    vis[x][y] = True
                    ans += max(0, h - heightMap[x][y])
                    heappush(pq, (max(h, heightMap[x][y]), x, y))
        return ans