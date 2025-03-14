from datetime import datetime, date
class Calculate_age:
    def __init__(self, today, birthday):
        self.today = today
        self.birthday = birthday
    def validation(self):
        date_is_ok = True
        birthday_date = [int(x) for x in (self.birthday).split('/')]
        if birthday_date[1] > 12 or birthday_date[2] > 31:
            date_is_ok = False
        elif birthday_date[1] == 2 and birthday_date[2] > 28:
            date_is_ok = False
        elif birthday_date[1] == 4 and birthday_date[2] > 30:
            date_is_ok = False
        elif birthday_date[1] == 6 and birthday_date[2] > 30:
            date_is_ok = False
        elif birthday_date[1] == 9 and birthday_date[2] > 30:
            date_is_ok = False
        elif birthday_date[1] == 11 and birthday_date[2] > 30:
            date_is_ok = False
        return date_is_ok
    def calculate(self):
        date1 = datetime.strptime(self.birthday, '%Y/%m/%d')
        date2 = datetime.strptime(self.today, '%Y-%m-%d')
        age = int((date2 - date1).days / 365.25)
        return print(age)


birthday = input()
today = str(date.today())
your_age = Calculate_age(today, birthday)
if your_age.validation():
    your_age.calculate()
else:
    print('WRONG')