class Father:
    def __init__(self, mood = "neutral"):
        self.mood = mood
    def greet(self):
        return "Hello!"
    def be_strict(self):
        self.mood = "strict"

class Mother:
    def __init__(self, mood = "neutral"):
        self.mood = mood
    def greet(self):
        return "Hi, honey!"
    def be_kind(self):
        self.mood = "kind"

class Daughter(Mother, Father):
    def __init__(self, mood = "neutral"):
        self.mood = mood

class Son(Father, Mother):
    def __init__(self, mood = "neutral"):
        self.mood = mood


f = Father()
print( f.greet())
f.be_strict()
print(f.mood)

print()

m = Mother()
print(m.greet())
m.be_kind()
print(m.mood)

print()

d = Daughter()
print(d.greet())
d.be_kind()
print(d.mood)
d.be_strict()
print(d.mood)

print()

s = Son()
print(s.greet())
s.be_strict()
print(s.mood)
s.be_kind()
print(s.mood)