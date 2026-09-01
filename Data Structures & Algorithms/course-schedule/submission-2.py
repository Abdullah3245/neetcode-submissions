class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses

        graph = [[] for _ in range(numCourses)]

        for reqs in prerequisites:
            graph[reqs[1]].append(reqs[0])
            in_degree[reqs[0]] += 1

        q = deque()
        topo_sort = set()

        for index, node in enumerate(in_degree):
            if node == 0:
                q.append(index)        
        
        while q:
            curr = q.popleft()
            topo_sort.add(curr)
            for neighbor in graph[curr]:
                if neighbor in topo_sort:
                    return False
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        print(len(topo_sort))
        return len(topo_sort) == numCourses