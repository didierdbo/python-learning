# List comprehensions provide a concise way to create lists.
# They consist of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses.
# The expressions can be anything, meaning you can put in all 
# kinds of objects in lists.

# So, instead of:
my_list = []
for c in 'hello':
    my_list.append(c)
print(my_list)

# We can do this:
my_list = [c for c in 'hello']
print(my_list)

# Creating a list with numbers from 0 to 99
my_list2 = [x for x in range(0, 100)]
print(my_list2)

# Multiplying each element in the list by 2
my_list3 = [x * 2 for x in my_list2]
print(my_list3)

# I want to keep only the even nombers in the list
my_list4 = [x for x in my_list2 if x % 2 == 0]
print(my_list4)

# It would be better to create a function more descriptive of what we want to do
def get_even_numbers(list):
    return [x for x in list if x % 2 == 0]
print(get_even_numbers(my_list2))
