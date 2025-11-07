class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Initialize number of islands
        no_of_islands = 0

        def dfs(x, y):
            # Mark as visited
            grid[x][y] = "0"
            # Check if neighbours are land
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                # Calculate nee positions
                new_x = x + dx
                new_y = y + dy
                # Check if new positions are within bounds of grid
                if (new_x < len(grid) and 0 <= new_x) and (
                    new_y < len(grid[0]) and 0 <= new_y
                ):
                    # If land, call dfs recursively
                    if grid[new_x][new_y] == "1":
                        dfs(new_x, new_y)

        # Call dfs for all nodes in the grid. This way we find the number of islands when dfs is called separately for a isolated land section
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    no_of_islands += 1

        # Return number of islands
        return no_of_islands

