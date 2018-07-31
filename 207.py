from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = {k:0 for k in range(numCourses)}
        dependency = defaultdict(set)
        for edge in prerequisites:
            if edge[1] in dependency[edge[0]]:
                return False
            indegree[edge[0]] += 1
            dependency[edge[1]].add(edge[0])
        queue = deque()
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)
        while queue:
            node = queue.popleft()
            numCourses -= 1
            for course in dependency[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        return True if numCourses == 0 else False