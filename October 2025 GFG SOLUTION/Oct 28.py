from collections import deque

class Solution:
    def nearest(self, grid):
        n, m = len(grid), len(grid[0])
        dist = [[-1 for _ in range(m)] for _ in range(n)]
        q = deque()
        
        # Enqueue all 1's and initialize their distance as 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        # Directions: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        
        return dist
