from abc import ABC, abstractmethod

class ChessPiece(ABC):
    @abstractmethod
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical
    @abstractmethod
    def can_move(self):
        pass

class King(ChessPiece):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def can_move(self, horizontal, vertical):
        if abs(self.horizontal - horizontal)<=1 and abs(ord(self.vertical) - ord(vertical))<=1:
            return "Can"
        else:
            return "Can't"

class Knight(ChessPiece):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def can_move(self, horizontal, vertical):
        if (abs(self.horizontal - horizontal)==2 and abs(ord(self.vertical) - ord(vertical))==1) or (abs(self.horizontal - horizontal)==1 and abs(ord(self.vertical) - ord(vertical))==2):
            return "Can"
        else:
            return "Can't"

lst = [King(5, 'b'), Knight(4, 'c')]

for i in lst:
    print(i.can_move(5, 'c'))
    print(i.can_move(2, 'd'))
    print(i.can_move(5, 'e'))
    print(i.can_move(4, 'd'))