import sys
import io

# Đảm bảo rằng stdout sử dụng UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
class Job:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Employee:
    def __init__(self, name):
        self.name = name
        self.total_time = 0

def schedule_jobs(jobs, employees):
    for i, job in enumerate(jobs):
        employee = employees[i % len(employees)]
        employee.total_time += job.duration
        print(f"{employee.name} is assigned to {job.name} for {job.duration} hours.")

def main():
    # Danh sách công việc
    jobs = [
        Job("A - Xây dựng bộ phận bên trong", 2),  # Chỉ truyền 2 tham số
        Job("B - Sửa chữa mái và sàn", 2),
        Job("C - Xây ống gom khói", 4),
        Job("D - Đổ bê tông và xây dựng", 7),
        Job("E - Xây cửa lò chịu nhiệt", 9),
        Job("F - Lắp đặt hệ thống kiểm soát", 7),
        Job("G - Lắp đặt thiết bị lọc khí", 13),
        Job("H - Kiểm tra và thử nghiệm", 15)
    ]

    # Danh sách nhân viên
    employees = [
        Employee("Employee 1"),
        Employee("Employee 2"),
        Employee("Employee 3"),
        Employee("Employee 4")
    ]

    # Xếp lịch công việc
    schedule_jobs(jobs, employees)

    # Tính tổng thời gian thực hiện
    total_time = sum(employee.total_time for employee in employees)
    print(f"Tổng thời gian thực hiện: {total_time} giờ.")

if __name__ == "__main__":
    main()
