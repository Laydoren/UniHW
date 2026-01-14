from abc import ABC, abstractmethod

class ChessPiece(ABC):
    @abstractmethod
    def __init__(self, vertical, horizontal):
        self.horizontal = horizontal
        self.vertical = vertical
    @abstractmethod
    def can_move(self):
        pass

class King(ChessPiece):
    def __init__(self, vertical, horizontal):
        self.horizontal = horizontal
        self.vertical = vertical

    def can_move(self, vertical, horizontal):
        if abs(self.horizontal - horizontal)<=1 and abs(ord(self.vertical) - ord(vertical))<=1:
            return "Can"
        else:
            return "Can't"

class Knight(ChessPiece):
    def __init__(self, vertical, horizontal):
        self.horizontal = horizontal
        self.vertical = vertical

    def can_move(self, vertical, horizontal):
        if (abs(self.horizontal - horizontal)==2 and abs(ord(self.vertical) - ord(vertical))==1) or (abs(self.horizontal - horizontal)==1 and abs(ord(self.vertical) - ord(vertical))==2):
            return "Can"
        else:
            return "Can't"

lst = [King('b', 5), Knight('c', 4)]

for i in lst:
    print(i.can_move('c', 5))
    print(i.can_move('d', 2))
    print(i.can_move('e', 5))
    print(i.can_move('d', 4))