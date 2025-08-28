from collections import deque

# Các hướng di chuyển: lên, xuống, trái, phải
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Hàm BFS để tìm số bước ngắn nhất tới các ô "O"
def bfs_closing_windows(grid):
    rows, cols = len(grid), len(grid[0])
    result = [[-1] * cols for _ in range(rows)]  # Ma trận kết quả với giá trị -1 (chưa đóng cửa sổ)
    queue = deque()

    # Tìm vị trí của tất cả bảo vệ "G" và thêm vào queue
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'G':
                queue.append((r, c, 0))  # Thêm tọa độ bảo vệ và số bước (0)
                result[r][c] = 0  # Bảo vệ không cần di chuyển để đóng cửa tại vị trí của chính mình

    # BFS
    while queue:
        r, c, steps = queue.popleft()
        
        # Duyệt qua 4 hướng di chuyển
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            
            # Kiểm tra xem vị trí mới có hợp lệ và có phải là ô "O" hoặc chưa được ghé thăm (-1)
            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 'O' and result[new_r][new_c] == -1:
                result[new_r][new_c] = steps + 1  # Cập nhật số bước
                queue.append((new_r, new_c, steps + 1))
    
    return result

# Dữ liệu đầu vào (bảng trạng thái ngân hàng)
grid = [
    ['O', 'O', 'O', 'O', 'O', 'G'],
    ['O', 'W', 'W', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'W', 'O'],
    ['O', 'O', 'G', 'O', 'W', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'G']
]

# Gọi hàm BFS để tìm đường đi ngắn nhất cho bảo vệ đóng cửa
result = bfs_closing_windows(grid)

# In kết quả
print("Output:")
for row in result:
    print(' '.join(map(str, row)))
