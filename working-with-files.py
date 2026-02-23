my_file = open('test.txt')
print(my_file.read())
my_file.seek(0)
print("************************")
print(my_file.readline())
my_file.close()

with open("test.txt", mode="a") as my_file:
    text = my_file.write("\nhhhheeeellllo line 3")
    print(text)
try:
    with open("test2.txt", mode="r") as my_file:
        print(my_file.readline())
except FileNotFoundError as err:
    print("file does not exist")
    raise err
except IOError as err:
    print("IO error")
    raise err
