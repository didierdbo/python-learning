def fibonacci(n):
    a, b = 0, 1
    curr = 0
    while curr < n:           
        yield a 
        a, b = b, a + b
        curr += 1
print([num for num in fibonacci(4)]) # [0, 1, 1, 2]

class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.curr = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr >= self.n:
          raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.curr += 1
        return result
    
print(list(FibonacciIterator(4))) # [0, 1, 1, 2]
    