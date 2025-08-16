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
        print(f"{employee.name} được giao cho {job.name} for {job.duration} tiếng.")

def main():
    # Danh sách công việc
    jobs = [
        Job("A - Xây dựng bộ phận bên trong", 2),
        Job("B - Sửa chữa mái và sàn",3),
        Job("C - Xây ống gom khói", 2),
        Job("D - Đổ bê tông và xây khung", 4),
        Job("E - Xây cửa lò chịu nhiệt", 4),
        Job("F - Lắp đặt hệ thống kiểm soát", 3),
        Job("G - Lắp đặt thiết bị lọc khí", 5),
        Job("H - Kiểm tra và thử nghiệm", 2)
        
        
        
    ]

    # Danh sách nhân viên
    employees = [
        Employee("2 Nhân viên"),
        Employee("3 Nhân viên"),
        Employee("2 Nhân viên "),
        Employee("4 Nhân viên"),
        Employee("4 sNhân viên"),
        Employee("3 Nhân viên "),
        Employee("5 Nhân viên"),
        Employee("2 Nhân viên"),
        
    ]

    # Xếp lịch công việc
    schedule_jobs(jobs, employees)

    # Tính tổng thời gian thực hiện
    total_time = sum(employee.total_time for employee in employees)
    print(f"Tổng thời gian thực hiện: {total_time} giờ.")

if __name__ == "__main__":
    main()
