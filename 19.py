class Multipler:
    def _init_(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number
    
mul = Multipler(5)
print(callable(mul))
print(mul(10))