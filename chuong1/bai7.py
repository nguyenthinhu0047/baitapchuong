import datetime

class Date:
    def __init__(self, day=datetime.date.today().day, month=datetime.date.today().month, year=datetime.date.today().year):
        self.day = day
        self.month = month
        self.year = year
    
    def display(self):
        print(f"Ngày: {self.day}")
        print(f"Tháng: {self.month}")
        print(f"Năm: {self.year}")
    
    def next(self):
        current_date = datetime.date(self.year, self.month, self.day)
        next_date = current_date + datetime.timedelta(days=1)
        self.day = next_date.day
        self.month = next_date.month
        self.year = next_date.year

date = Date(10, 9, 2023)
date.display()

date.next()
date.display()
