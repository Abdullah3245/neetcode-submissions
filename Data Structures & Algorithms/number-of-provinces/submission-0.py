class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS, COLS = len(isConnected), len(isConnected[0])

        graph = [[] for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        def dfs(node, prev, visited):
            nonlocal graph
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == prev: 
                    continue
                if neighbor in visited:
                    continue
                dfs(neighbor, node, visited)
        
        visited = set()
        cc = 0
        for node in range(ROWS):
            if node not in visited:
                dfs(node, -1, visited)
                cc += 1
        
        return cc
