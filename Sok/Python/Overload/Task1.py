class Negator:
    @staticmethod
    def neg(smt):
        if isinstance(smt, bool):
            return not smt
        elif isinstance(smt,(int, float)):
            return -smt
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

print(Negator.neg(2837))
print(Negator.neg(0.1))
print(Negator.neg(True))
print(Negator.neg(False))
print(Negator.neg("check this out"))