from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def BFS(self, u):
        visited = [False] * (max(self.graph.keys() | {v for adj in self.graph.values() for v in adj}) + 1)
        queue = []
        visited[u] = True
        queue.append(u)
        while queue:
            u = queue.pop(0)
            print(u + 1, end= "")
            for i in self.graph[u]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 6)
    print("DFS start with vertex 4")
    g.BFS(1)