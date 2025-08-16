# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#     def DFSUtil(self, v, visited):
#         visited[v] = True
#         print(v, end = "")
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.DFSUtil(i, visited)
#     def DFS(self, v):
#         visted = [False] * (max(self.graph) + 1)
#         self.DFSUtil(v, visted)
        
# if __name__ == "__main__":
#     g = Graph()
#     g.addEdge(0, 1)
#     g.addEdge(0, 2)
#     g.addEdge(1, 2)
#     g.addEdge(2, 0)
#     g.addEdge(2, 3)
#     g.addEdge(3, 3)
#     print("DFS start with vertex 2")
#     g.DFS(2)
    
    
# # Thay 0 là HCM, 1 BD, 2 ĐN, 3 BRVT
# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
#         self.vertices = {}  
    
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
    
#     def addVertex(self, key, location):
#         self.vertices[key] = location
    
#     def DFSUtil(self, v, visited):
#         visited[v] = True
#         print(self.vertices[v], end=" ")
#         for i in self.graph[v]:
#             if not visited[i]:
#                 self.DFSUtil(i, visited)
    
#     def DFS(self, v):
#         visited = [False] * (max(self.graph) + 1)
#         self.DFSUtil(v, visited)

# if __name__ == "__main__":
#     g = Graph()
#     g.addVertex(0, "HCM") #  Hàm thêm đỉnh với các tên tương ứng 
#     g.addVertex(1, "BD")
#     g.addVertex(2, "ĐN")
#     g.addVertex(3, "BRVT")
    
    
#     g.addEdge(0, 1) 
#     g.addEdge(0, 2)  
#     g.addEdge(1, 2)  
#     g.addEdge(2, 0)  
#     g.addEdge(2, 3)  
#     g.addEdge(3, 3)  
#     print("DFS starting with vertex ĐN:")
#     g.DFS(0)
    
    
# # Bài thêm
# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#     def DFSUtil(self, v, visited):
#         visited[v] = True
#         print(v, end = "")
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.DFSUtil(i, visited)
#     def DFS(self, v):
#         visted = {v: False for v in self.graph}
#         self.DFSUtil(v, visted)

# if __name__ == "__main__":
#     g = Graph()
#     g.addEdge("A", "B")
#     g.addEdge("A", "D")
#     g.addEdge("B", "C")
#     g.addEdge("B", "F")
#     g.addEdge("C", "E")
#     g.addEdge("C", "G")
#     g.addEdge("C", "H")
#     g.addEdge("G", "H")
#     g.addEdge("G", "E")
#     g.addEdge("D", "F")
#     g.addEdge("F", "A")
#     g.addEdge("E", "B")
#     g.addEdge("E", "F")
#     g.addEdge("H", "A")
#     print("DFS start with vertex A")
#     g.DFS("A")
