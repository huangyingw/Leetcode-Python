from collections import defaultdict, deque


class Solution:
    # BFS
    def alienOrder(self, words: List[str]) -> str:
        counter, graph = {}, {}
        for word in words:
            for c in word:
                counter[c] = 0
                graph[c] = set()
        for i in range(1, len(words)):
            prev, curr = words[i - 1], words[i]
            l = min(len(prev), len(curr))
            for j in range(l):
                if prev[j] != curr[j]:
                    if curr[j] not in graph[prev[j]]:
                        graph[prev[j]].add(curr[j])
                        counter[curr[j]] += 1
                    break
        q = deque()
        for k, v in counter.items():
            if v == 0:
                q.append(k)
        result = ''
        while q:
            curr = q.popleft()
            result += curr
            for child in graph[curr]:
                counter[child] -= 1
                if counter[child] == 0:
                    q.append(child)
        return result if len(result) == len(graph.keys()) else ''

        #     # DFS
        #     def alienOrder(self, words: List[str]) -> str:
        #         visited, graph = {}, {}
        #         for word in words:
        #             for c in word:
        #                 graph[c] = set()
        #                 visited[c] = 0
        #         for i in range(1, len(words)):
        #             prev, curr = words[i-1], words[i]
        #             l = min(len(prev), len(curr))
        #             for j in range(l):
        #                 if prev[j] != curr[j]:
        #                     graph[prev[j]].add(curr[j])
        #                     break
        #         result = []
        #         for k in graph.keys():
        #             if not self.dfs(k, visited, graph, result):
        #                 return ''
        #         return ''.join(result)

        #     def dfs(self, c, visited, graph, result):
        #         if visited[c] == 1: return True
        #         if visited[c] == -1: return False
        #         visited[c] = -1
        #         for child in graph[c]:
        #             if not self.dfs(child, visited, graph, result):
        #                 return False
        #         visited[c] = 1
        #         result.insert(0, c)
        #         return True