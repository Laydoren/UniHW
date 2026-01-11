class Counter:
    def __init__(self, start=0):
        self.value = start
    def inc(self, n=None):
        if n == None:
            self.value += 1
        else:
            self.value += n
        return self.value
    
    def dec(self, n=None):
        if n == None:
            self.value -= 1
        else :
            self.value -= n
        if self.value < 0:
            self.value = 0
        return self.value 

class NonDecCounter(Counter):
    def __init__(self, start=0):
        super().__init__(start)
    
    def dec(self, n=None):
        pass

class LimitedCounter(Counter):
    def __init__(self, start=0,limit = 10):
        super().__init__(start)
        self.limit = limit
    
    def inc(self, n=None):
        if n == None:
            self.value += 1
        else:
            self.value += n
        if self.value > self.limit:
            self.value = self.limit 
        return self.value

count = Counter(1)
ndcount = NonDecCounter(10)
lcount = LimitedCounter(5, limit=34)

print("Counter:")
print(count.inc())
print(count.inc(9))
print(count.dec())
print(count.dec(23))
print(count.value)


print("NonDecCounter:")
print(ndcount.inc())
print(ndcount.inc(30))
print(ndcount.dec())
print(ndcount.dec(70))
print(ndcount.value)

print("LimitedCounter:")
print(lcount.inc())
print(lcount.inc(2))
print(lcount.inc(4))
print(lcount.dec(8))
print(lcount.inc(35))
print(lcount.value)