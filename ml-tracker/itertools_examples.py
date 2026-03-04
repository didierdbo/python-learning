import itertools  
# chain — concatène des iterables
list(itertools.chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# islice — slice un générateur (impossible autrement)
list(itertools.islice(range(1000), 5))  # [0, 1, 2, 3, 4]

# groupby — regroupe des éléments consécutifs
data = [("a", 1), ("a", 2), ("b", 3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a [('a', 1), ('a', 2)]
# b [('b', 3)]
