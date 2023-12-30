from datetime import date

class Employee:
    def __init__(self, full_name, birth_date, hire_date):
        self.full_name = full_name
        self.birth_date = birth_date
        self.hire_date = hire_date

employee = Employee("Nguyễn Văn A", date(1990, 1, 1), date(2021, 5, 10))

print("Họ tên:", employee.full_name)
print("Ngày sinh:", employee.birth_date)
print("Ngày vào công ty:", employee.hire_date)