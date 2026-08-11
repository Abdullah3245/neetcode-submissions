class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs_visit(graph, vertex, color) -> bool:
            color[vertex] = GREY

            for neighbor in graph[vertex]:
                if color[neighbor] == GREY:
                    return False  # back edge

                if color[neighbor] == WHITE and not dfs_visit(graph, neighbor, color):
                    return False

            color[vertex] = BLACK
            return True

        graph = [[] for _ in range(numCourses)]

        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        WHITE, GREY, BLACK = 0, 1, 2

        color = [WHITE] * numCourses

        for vertex in range(numCourses):
            if color[vertex] == WHITE and not dfs_visit(graph, vertex, color):
                return False
        return True
