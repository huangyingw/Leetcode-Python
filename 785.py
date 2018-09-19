class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph: return False
        visited = {}

        def dfs(pos):
            for j in graph[pos]:
                if j in visited:
                    if visited[j] == visited[pos]: return False
                else:
                    visited[j] = 1 - visited[pos]
                    if not dfs(j): return False
            return True

        for i in range(len(graph)):
            if i not in visited:
                visited[i] = 0
            if not dfs(i): return False
        return True