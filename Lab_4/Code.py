import sys
import io

# Đảm bảo đầu ra hỗ trợ mã hóa UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        
    def minDistance(self, dist, sptSet):
        min_value = float('inf')
        min_index = -1
        
        for v in range(self.V):
            if dist[v] < min_value and not sptSet[v]:
                min_value = dist[v]
                min_index = v
        
        return min_index
    
    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        
        sptSet = [False] * self.V
        prev = [None] * self.V  # Mảng để theo dõi đỉnh trước

        for count in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            
            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and \
                   dist[v] > (dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    prev[v] = u  # Cập nhật đỉnh trước

        return dist, prev

    def get_path(self, prev, node):
        path = []
        while node is not None:
            path.append(chr(node + 97))  # Chuyển đổi chỉ số sang ký tự (0 -> 'a', 1 -> 'b', ...)
            node = prev[node]
        return path[::-1]  # Đảo ngược đường đi

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

# Bước 1: Tính khoảng cách từ a (0) đến g (6)
dist, prev = g.dijkstra(0)

# Tính đường đi từ a đến g
path_a_to_g = g.get_path(prev, 6)
path_str = " -> ".join(path_a_to_g)  # Định dạng đường đi

# Độ dài đi từ a đến g
a_to_g_distance = dist[6]

# In kết quả
print(f"Đường đi từ a đến g là: {path_str}")
print(f"Độ dài đi từ a đến g là: {a_to_g_distance}")
