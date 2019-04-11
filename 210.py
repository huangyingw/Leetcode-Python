from collections import defaultdict
from collections import deque

## DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, visited = {}, {}
        for c in range(numCourses):
            graph[c] = set()
            visited[c] = 0
        for p in prerequisites:
            graph[p[1]].add(p[0])

        result = []
        for key in graph.keys():
            if not self.dfs(key, result, graph, visited):
                return []
        return result

    def dfs(self, curr, result, graph, visited):
        if visited[curr] == 1: return True
        if visited[curr] == -1: return False
        visited[curr] = -1
        for child in graph[curr]:
            if not self.dfs(child, result, graph, visited):
                return False
        visited[curr] = 1
        result.insert(0, curr)
        return True

## BFS
# class Solution:
#     def findOrder(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: List[int]
#         """
#         order = []
#         dependency = defaultdict(set)
#         indegree = {k: 0 for k in range(numCourses)}
#         for edge in prerequisites:
#             indegree[edge[0]] += 1
#             dependency[edge[1]].add(edge[0])
#
#         queue = deque()
#         for k, v in indegree.items():
#             if v == 0:
#                 queue.append(k)
#
#         while queue:
#             node = queue.popleft()
#             order.append(node)
#             for course in dependency[node]:
#                 indegree[course] -= 1
#                 if indegree[course] == 0:
#                     queue.append(course)
#         return order if len(order) == numCourses else []