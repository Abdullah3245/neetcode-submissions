class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS, COLS = len(isConnected), len(isConnected[0])
        
        def dfs(node, visited):
            visited.add(node)

            for neighbor in range(ROWS):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor , visited)
        
        visited = set()
        cc = 0
        for node in range(ROWS):
            if node not in visited:
                dfs(node, visited)
                cc += 1
        
        return cc
