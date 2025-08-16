import sys
sys.stdout.reconfigure(encoding='utf-8')  # Thiết lập hỗ trợ mã hóa đầu ra để hỗ trợ tiếng việt

# Khởi tạo danh sách các công việc giảm dần
t = [2, 5, 8, 1, 5, 1]
t.sort(reverse=True)  # t.sort là biến để tìm ra danh sách giảm dần

# Danh sách công việc cho 3 máy
m = [[] for _ in range(3)]
k = [0] * len(m)

# Hàm tìm máy có nhiều thời gian rảnh nhất
def min_machine(m, k):
    # Tính tổng thời gian của từng máy
    for i in range(len(m)):
        k[i] = sum(m[i])

    min_time = min(k)

    # In ra tình hình công việc của từng máy để kiểm tra
    for i in range(len(m)):
        print(f"Máy {i + 1} hiện có công việc: {m[i]} với tổng thời gian: {k[i]}")

    return k.index(min_time)

# Hàm xếp lịch
def schedule(t, m, k):
    # Trong khi vẫn còn công việc
    while t:
        # Lấy công việc từ danh sách t đã sắp xếp giảm dần
        job = t.pop(0)  # Lấy công việc lớn nhất
        
        # Tìm máy có thời gian ít nhất
        machine_idx = min_machine(m, k)  # Gọi hàm với 2 tham số
        
        # Gán công việc cho máy có ít thời gian nhất
        m[machine_idx].append(job)
        
        # Cập nhật thời gian của máy đó
        k[machine_idx] += job

# Gọi hàm xếp lịch
schedule(t, m, k)

# In ra tình hình công việc sau khi xếp lịch
print("Danh sách phân công công việc cho các máy:")
for i in range(len(m)):
    print(f"Máy {i + 1}: {m[i]} với tổng thời gian: {k[i]}")
