class Bachelor:
    def __init__(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark

    def getScholarship(self):
        if self.averageMark == 5:
            return 10000
        elif self.averageMark > 3:
            return 5000
        else:
            return 0


class Undergraduate(Bachelor):
    def __init__(self, firstName, lastName, group, averageMark, scienceWork):
        super().__init__(firstName, lastName, group, averageMark)
        self.researchWork = scienceWork

    def getScholarship(self):
        if self.averageMark == 5:
            return 15000
        elif self.averageMark > 3:
            return 7500
        else:
            return 0


spisok = [
    Bachelor("Golb", "Grenkin", "14555", 4),
    Bachelor("Vova", "Volvo", "31222", 5),
    Undergraduate("Alina", "Chessova", "12345", 3, "PuskinProstoClassniChuvak"),
    Undergraduate("Olga", "Morgon", "54321", 5, "DRY or never TRY")
]

for i in spisok:
    print(i.getScholarship())