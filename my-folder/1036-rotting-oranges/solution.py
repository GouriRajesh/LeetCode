class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Count of fresh oranges
        fresh_orange_count = 0
        # Rotten oranges Queue
        rotten_orange_queue = deque()

        # Count fresh oranges and add rotten oranges to the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_orange_count += 1
                if grid[i][j] == 2:
                    rotten_orange_queue.append([i, j])

        # Initialize minutes passed
        minutes_passed = 0
        # While there are rotten oranges and fresh oranges to rot
        while rotten_orange_queue and fresh_orange_count > 0:
            # Repeatedly check for all rotten oranges simultaneously
            for _ in range(len(rotten_orange_queue)):
                # Get rotten orange coordinates
                row, col = rotten_orange_queue.popleft()
                # New directions to move in
                for r, c in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    # New coodinates to check
                    new_row = row + r
                    new_col = col + c
                    # Remain in boundary of grid
                    if (new_row >= 0 and new_row < len(grid)) and (
                        new_col >= 0 and new_col < len(grid[0])
                    ):
                        # If fresh orange
                        if grid[new_row][new_col] == 1:
                            # Rot it
                            grid[new_row][new_col] = 2
                            # Add to rotten orange queue
                            rotten_orange_queue.append([new_row, new_col])
                            # Reduce fresh orange count
                            fresh_orange_count -= 1
            # After checking all rotten oranges simultaneously -> minute passed
            minutes_passed += 1

        # If fresh orange remains
        if fresh_orange_count != 0:
            return -1
        # If all oranges rot
        return minutes_passed

