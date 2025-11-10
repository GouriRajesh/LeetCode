class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Store the topo sort result
        res = []
        # Create adjacency list
        adj_list = [[] for _ in range(numCourses)]
        # Maintain an indegree array
        indegree = [0] * numCourses

        # Create the adjacency list and update indegree array
        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]
            adj_list[prereq].append(course)
            indegree[course] += 1

        # Add nodes with indegree 0 to queue
        queue = deque([])
        for node in range(len(indegree)):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            # Pop from queue and check neighbours
            node = queue.popleft()
            res.append(node)
            for neighbour in adj_list[node]:
                # Reduce indegree of neighbours
                indegree[neighbour] -= 1
                # If indegree reaches 0, append to queue
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        # If result != length of courses -> cycle exists -> return False
        if len(res) != numCourses:
            return False
        return True

