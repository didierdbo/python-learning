def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(5):
    print(item)

print("----------------")
g = generator_function(5)
next(g)
next(g)
print(next(g))
print(next(g))
print("----------------")
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print("Before")
            item = next(iterator)
            print("After")
        except StopIteration:
            print("The end.")
            break
        else:
            print(item)
special_for([1, 2, 3])
print("----------------")
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(1, 10)
for i in gen:
    print(i)

print("----------------")
def fib(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        a, b = b, a + b
        
for item in fib(10):
    print(item)
