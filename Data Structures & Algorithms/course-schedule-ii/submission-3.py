class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        inDegree = [-1] * numCourses

        for curr in prerequisites:
            graph[curr[1]].append(curr[0])
            inDegree[curr[0]] = 0
            inDegree[curr[1]] = 0


        for node in range(numCourses):
            for neighbor in graph[node]:
                inDegree[neighbor] += 1

        sources = deque()

        for index, degree in enumerate(inDegree):
            if degree == 0:
                sources.append(index)

        topo_sort = []

        while sources:
            curr = sources.popleft()
            topo_sort.append(curr)
            for neighbor in graph[curr]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    sources.append(neighbor)
        
        for index, degree in enumerate(inDegree):
            if degree == -1:
                topo_sort.append(index)


        if len(topo_sort) == numCourses:
            return topo_sort
        else:
            return []        