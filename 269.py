from collections import defaultdict
from collections import deque

class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        total_chars = set()
        for word in words:
            for c in word:
                total_chars.add(c)
        result = ''
        dependency, incoming_degree = defaultdict(set), {c:0 for c in total_chars}
        for i in range(1, len(words)):
            prev, curr = words[i-1], words[i]
            l = min(len(prev), len(curr))
            for j in range(l):
                if prev[j] == curr[j]:
                    continue
                if not curr[j] in dependency[prev[j]]:
                    dependency[prev[j]].add(curr[j])
                    incoming_degree[curr[j]] += 1
                break
        queue = deque()
        for k, v in incoming_degree.items():
            if v == 0:
                queue.append(k)
        while queue:
            node = queue.popleft()
            result += node
            if node not in dependency:
                continue
            for child in dependency[node]:
                incoming_degree[child] -= 1
                if incoming_degree[child] == 0:
                    queue.append(child)
        if len(result) != len(total_chars): return ''
        return result