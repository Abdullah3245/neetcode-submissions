class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs_visit(graph, vertex, color):
            color[vertex] = 1
            for neighbors in graph[vertex]:
                if color[neighbors] == 0:
                    dfs_visit(graph, neighbors, color)
                
            color[vertex] = 2
        # We will start by constructing a graph
        graph = [[] for _ in range(n + 1)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # We will perform DFS to get all the connected components
        connected_components = 0
        color = [0] * n
        for vertex in range(n):
            if color[vertex] == 0:
                dfs_visit(graph, vertex, color)
                connected_components += 1
        return connected_components