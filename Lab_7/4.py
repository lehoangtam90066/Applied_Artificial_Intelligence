import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
from simpleai.search import CspProblem, backtrack

# Hàm kiểm tra ràng buộc: không có 2 quân hậu nào được đặt trong cùng hàng, cột, hoặc đường chéo
def constraint(variables, values):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            # Kiểm tra cùng cột hoặc đường chéo
            if values[i] == values[j] or abs(values[i] - values[j]) == abs(variables[i] - variables[j]):
                return False
    return True

# Khởi tạo biến và miền giá trị cho mỗi quân hậu
n = 8
variables = range(n)
domains = {var: range(n) for var in variables}

# Tạo bài toán và thêm ràng buộc
constraints = [(variables, constraint)]  # Đặt hàm ràng buộc vào tuple với biến liên quan

problem = CspProblem(variables, domains, constraints)

# Nhập vị trí quân hậu từ người dùng và kiểm tra ràng buộc
positions = []  # Khởi tạo danh sách rỗng
print(f"Nhập vị trí quân hậu trên bảng {n}x{n}:")
for i in variables:
    row = int(input(f"Nhập vị trí hàng của quân hậu thứ {i + 1} (0 đến {n - 1}): "))
    positions.append(row)

# Kiểm tra ràng buộc với vị trí quân hậu nhập vào
if constraint(variables, positions):
    print("Vị trí quân hậu hợp lệ. Không có quân hậu nào trên cùng dòng, cột, hoặc đường chéo.")
else:
    print("Vị trí quân hậu không hợp lệ. Có quân hậu trên cùng dòng, cột, hoặc đường chéo.")
