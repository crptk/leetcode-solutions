class Solution:
    def DFS(self, grid, i, j):
        rows, cols = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == '0':
            return

        grid[i][j] = '0'    
        left = self.DFS(grid, i, j-1)
        right = self.DFS(grid, i, j+1)
        down = self.DFS(grid, i+1, j)
        up = self.DFS(grid, i-1, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS(grid, i, j)
                    count += 1
        return count

'''
solution by Edrees

Simple solution, if the current cell is 1, then run DFS on it and mark all cells seen as "0" (water/visited)
Otherwise skip. 
Time complexity: O(m*n)
'''
