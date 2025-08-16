import sys
import io

# Đảm bảo đầu ra hỗ trợ mã hóa UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(f"{node} \t\t {dist[node]}")
            
    def minDistance(self, dist, sptSet):
        min_value = float('inf')
        min_index = -1
        
        for v in range(self.V):
            if dist[v] < min_value and not sptSet[v]:
                min_value = dist[v]
                min_index = v
        
        return min_index
    
    def dijkstra(self, src, tranh=None):
        dist = [float('inf')] * self.V
        dist[src] = 0
        
        sptSet = [False] * self.V
        
        for count in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            
            # Nếu đỉnh hiện tại là đỉnh cần tránh thì bỏ qua
            if tranh is not None and u == tranh:
                continue
            
            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and \
                   dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        
        return dist

# Khởi tạo đồ thị
g = Graph(10)  # Số lượng đỉnh từ a đến j
g.graph = [
    # a, b, c, d, e, f, g, h, i, j
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # a
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],  # b
    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],  # c
    [10, 0, 0, 0, 4, 0, 0, 0, 0, 0],  # d
    [0, 0, 0, 0, 0, 3, 5, 12, 0, 0],  # e
    [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],   # f
    [0, 0, 0, 0, 0, 0, 0, 6, 0, 0],   # g
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 7],   # h
    [0, 0, 0, 9, 0, 0, 0, 0, 0, 0],   # i
    [0, 0, 0, 0, 0, 0, 0, 0, 8, 0]    # j
]


tranh_f = 5
diem_a_qua_i_tranh_f = g.dijkstra(0, tranh=tranh_f)[8]


print(f"Khoảng cách từ a đến i mà không qua c là: {diem_a_qua_i_tranh_f}")


