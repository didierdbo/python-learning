def accumulator():
    total = 0
    while True:
        value = yield total   # yield retourne ET reçoit une valeur
        total += value
        print(value, total)

gen = accumulator()
next(gen)          # initialise (avance jusqu'au premier yield)
gen.send(10)       # envoie 10 → total = 10
gen.send(5)        # envoie 5 → total = 15