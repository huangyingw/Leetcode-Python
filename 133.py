# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        mapping = dict()
        def clone(root):
            if not root: return None
            if root.label in mapping:
                return mapping[root.label]
            new_root = UndirectedGraphNode(root.label)
            mapping[root.label] = new_root
            for n in root.neighbors:
                new_root.neighbors.append(clone(n))
            return new_root
        return clone(node)