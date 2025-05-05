class Countdown:
    def __init__(self, start):
        self.start = start

    def _iter_(self):
        return self
    
    def _next_(self):
        if self.start < 0:
            raise StopIteration
        Value = self.start
        self.start -=1
        return Value
    
for num in Countdown(5):
    print(num)