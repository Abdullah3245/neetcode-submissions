class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for req in prerequisites:
            graph[req[1]].append(req[0])
            in_degree[req[0]] += 1
        
        q = deque()

        for index, degree in enumerate(in_degree):
            if degree == 0:
                q.append(index)
        
        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            for neighbour in graph[curr]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    q.append(neighbour)
        
        if len(order) == numCourses:
            return order
        else:
            return []
