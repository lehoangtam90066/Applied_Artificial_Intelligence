from collections import deque
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Bước đi của quân mã 
quan_ma = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

# Kiểm tra vị trí con ngựa có hợp lệ không
def vi_tri(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 1

# Hàm tìm đường đi ngắn nhất
def duong_di(board, start, target):
    # Kiểm tra nếu vị trí start hoặc target không hợp lệ (nằm trên ô không hợp lệ)
    if not (vi_tri(start[0], start[1], board) and vi_tri(target[0], target[1], board)):
        return "Quân mã hoặc mục tiêu nằm trên ô không hợp lệ!", []

    # Vị trí hiện tại, số bước di chuyển
    queue = deque([(start, 0)])
    # Lưu lại các vị trí đã đi qua và danh sách các bước trước đó
    visit = set([start])
    prev = {start: None}  # Dictionary lưu lại các bước trước của mỗi vị trí
    
    while queue:
        (x, y), steps = queue.popleft()
        
        # Nếu đã đến mục tiêu thì trả về số bước và đường đi
        if (x, y) == target:
            path = get_path(prev, (x, y))
            return steps, path
        
        # Duyệt qua các bước đi của quân mã
        for dx, dy in quan_ma:
            new_x, new_y = x + dx, y + dy 
            
            # Kiểm tra các bước đi có hợp lệ không
            if vi_tri(new_x, new_y, board) and (new_x, new_y) not in visit:
                visit.add((new_x, new_y))
                prev[(new_x, new_y)] = (x, y)  # Lưu lại vị trí trước đó
                queue.append(((new_x, new_y), steps + 1))
    
    # Không tìm thấy đường đi
    return "Không có đường đi tới đích!", []

# Hàm tìm đường đi cụ thể từ `prev`
def get_path(prev, node):
    path = []
    while node is not None:
        path.append(node)  # Lưu lại tọa độ vị trí
        node = prev[node]
    return path[::-1]  # Đảo ngược để trả về đường đi đúng thứ tự

# Bảng cờ với các vị trí hợp lệ (1 là ô hợp lệ, 0 là ô không thể đi)
board = [
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0]
]

# Hàm để tìm đường đi giữa tất cả các ô hợp lệ
def tim_duong_di_tat_ca_vi_tri(board):
    rows = len(board)
    cols = len(board[0])

    for x in range(rows):
        for y in range(cols):
            if board[x][y] == 1:  # Kiểm tra ô hợp lệ (1 là ô hợp lệ)
                # Duyệt qua tất cả các vị trí khác
                for i in range(rows):
                    for j in range(cols):
                        if (x, y) != (i, j) and board[i][j] == 1:
                            start = (x, y)
                            target = (i, j)
                            duong_di_ngan, duong_di_path = duong_di(board, start, target)

                            # Kiểm tra kết quả
                            if isinstance(duong_di_ngan, int):
                                print(f"Từ {start} đến {target}: Số bước ít nhất là {duong_di_ngan}")
                                print("Đường đi cụ thể:")
                                for step in duong_di_path:
                                    print(step)
                                print("-" * 40)
                            else:
                                print(f"Từ {start} đến {target}: {duong_di_ngan}")
                                print("-" * 40)

# Chạy hàm tìm đường đi trên tất cả các vị trí hợp lệ
tim_duong_di_tat_ca_vi_tri(board)
