class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs_visit(vertex, graph, parent, visited) -> bool:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                # if not dfs_visit(neighbor, graph, vertex, visited):
                #     return False
                visited.add(neighbor)
                dfs_visit(neighbor, graph, vertex, visited)
            return True

            
        # We will start by constructing a graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # Now we check for cycles and before DFS for this
        visited = set()
        if not dfs_visit(0, graph, -1, visited):
            return False
        return len(visited) == n