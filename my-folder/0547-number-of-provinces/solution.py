class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0

        def dfs(node):
                visited.add(node)
                for neighbour in range(len(isConnected)):
                    if isConnected[node][neighbour] ==1 and neighbour not in visited:
                        dfs(neighbour)
                        

        for i in range(len(isConnected)):
            if i not in visited:
                count +=1
                dfs(i)

        return count


               
