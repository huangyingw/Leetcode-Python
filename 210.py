from collections import defaultdict
from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        order = []
        dependency = defaultdict(set)
        indegree = {k: 0 for k in range(numCourses)}
        for edge in prerequisites:
            indegree[edge[0]] += 1
            dependency[edge[1]].add(edge[0])

        queue = deque()
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)

        while queue:
            node = queue.popleft()
            order.append(node)
            for course in dependency[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        return order if len(order) == numCourses else []