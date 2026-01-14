from abc import ABC, abstractmethod

class CountryDate(ABC):
    @abstractmethod
    def format(self):
        pass
    @abstractmethod
    def iso_format(self):
        pass

class USADate(CountryDate):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return  f"{self.month}-{self.day}-{self.year}"

    def iso_format(self):
        return  f"{self.year}-{self.month}-{self.day}"

class ItalianDate(CountryDate):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return  f"{self.day}/{self.month}/{self.year}"

    def iso_format(self):
        return  f"{self.year}-{self.month}-{self.day}"


usa_date = USADate(2020, 1, 1)
print(usa_date.iso_format())
print(usa_date.format())

ita_date = ItalianDate(2020, 1, 1)
print(ita_date.iso_format())
print(ita_date.format())