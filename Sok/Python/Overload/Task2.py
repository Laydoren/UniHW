from datetime import date

class BirthInfo:
    def __init__(self, birth_date):
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif isinstance(birth_date, str):
            try:
                self.birth_date = date.fromisoformat(birth_date)
            except:
                raise TypeError("Аргумент переданного типа не поддерживается")
        elif isinstance(birth_date, (list, tuple)):
            try:
                self.birth_date = date(*birth_date)
            except:
                raise TypeError("Аргумент переданного типа не поддерживается")
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year

        if (today.month, today.day) <= (self.birth_date.month, self.birth_date.day):
            age -= 1

        return age

b1 = BirthInfo(date(2005, 7, 25))
b2 = BirthInfo("2012-01-01")
print(b1.age)
print(b2.age)