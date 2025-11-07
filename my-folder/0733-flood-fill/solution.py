class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        # Store initial source colour to check neighbours
        source_colour = image[sr][sc]
        # If source colour == target colour -> No updates needed
        if source_colour == color:
            return image
        # Enqueue the source position
        queue = deque([(sr, sc)])

        # While there are adjacent neighbours to check
        while queue:
            # Get current position
            x, y = queue.popleft()
            # Check if colour == source colour
            if image[x][y] == source_colour:
                # If yes -> update the colour
                image[x][y] = color
                # Check adjacent neighbours
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    new_x = x + dx
                    new_y = y + dy
                    # Make sure new neighbours are within the bounds of image
                    if (new_x < len(image) and 0 <= new_x) and (
                        new_y < len(image[0]) and 0 <= new_y
                    ):
                        # If neighbours colour == source colour -> Add to queue
                        if image[new_x][new_y] == source_colour:
                            queue.append([new_x, new_y])
        return image

