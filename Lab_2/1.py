from collections import defaultdict

class Graph:

    def __init__(self):

        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def BFS(self, u):

        visited = [False] * (len(self.graph))


        queue = []


        visited[u] = True
        queue.append(u)

        while queue:

            u = queue.pop(0)
            print(u + 1, end=" ")


            for i in self.graph[u]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 0)
g.addEdge(2, 4)
g.addEdge(3, 1)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 1)
g.addEdge(4, 3)
g.addEdge(4, 5)
g.addEdge(5, 4)
g.addEdge(5, 3)


print("BFS starts with vertex 1")
g.BFS(0)
