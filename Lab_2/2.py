from collections import defaultdict
class Graph:

    def __init__(self):

        self.graph = [[0] * 5 for i in range (5)]
        self.edges = []


    def addEdge(self, u, v, w):
        self.graph[u][v] = w


    def BFS(self, u):

        visited = [False] * (len(self.graph)+1)


        queue = []


        visited[u] = True
        queue.append(u)
        s = u
        while queue:

            u = queue.pop(0)
            print(u + 1, end=" ")

            a = []
            b = []

            for i in range(len(self.graph)):

                if self.graph[u][i] > 0:
                    if not visited[i]:
                        a.append(self.graph[u][i])
                        b.append(i)
                    
            if len(a) and len(b):
                p = b[a.index(min(a))]
                queue.append(p)
                self.edges.append([u, p, self.graph[u][p]])
                visited[p] = True

g = Graph()
g.addEdge(0, 1, 1)
g.addEdge(0, 2, 2)
g.addEdge(0, 3, 7)
g.addEdge(0, 4, 5)
g.addEdge(1, 0, 1)
g.addEdge(1, 2, 4)
g.addEdge(1, 3, 4)
g.addEdge(1, 4, 3)
g.addEdge(2, 1, 4)
g.addEdge(2, 3, 1)
g.addEdge(2, 4, 2)
g.addEdge(2, 0, 2)
g.addEdge(3, 0, 7)
g.addEdge(3, 1, 4)
g.addEdge(3, 2, 1)
g.addEdge(3, 4, 3)
g.addEdge(4, 0 ,5)
g.addEdge(4, 1, 3)

print("BFS starts with vertex 1")
g.BFS(0)

print("\n")
sum = 0
for item in g.edges:
    print((item[0]+1), ",", (item[1]+1), "-->", (item[2]))

