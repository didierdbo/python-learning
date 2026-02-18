from utility.metrics import performance


# Question 1: 
# Write a program which will find all such numbers which are divisible by 7 
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence 
# on a single line.

@performance
def multiples_of_seven():
    l = []
    next = (int(2000 / 7) + 1) * 7
    while next <= 3200:
        if not (next % 5 == 0):
            l.append(next)
        next += 7
    print(','.join(str(x) for x in l))

multiples_of_seven()
print("------------------")

@performance
def multiples_of_seven2():
    print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")
multiples_of_seven2()
print("------------------")

# Fastest implementation using generators
def multiples_of_seven_gen():
    next = (int(2000 / 7) + 1) * 7
    while next <= 3200:
        if not (next % 5 == 0):
            yield next
        next += 7

@performance
def multiples_of_seven3():
    print(','.join(str(x) for x in multiples_of_seven_gen()))

multiples_of_seven3()
print("------------------")

