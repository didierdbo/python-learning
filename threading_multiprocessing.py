import threading
import requests


# def fetch(i, url:str, results: dict[int, str]) -> None:
#     res = requests.get(url).text
#     results[i] = res


# results = dict()
# urls = ['https://www.google.com/', 'https://www.google.de/', 'https://www.google.fr/']
# threads = [threading.Thread(target=fetch, args=(i, urls[i], results)) for i in range(len(urls))]

# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print(results.keys())

# from utility import utils
# from multiprocessing import Process, Queue

# def factorial(n):
#     if n <= 1:
#         return n
#     return n * factorial(n-1)
# q = Queue(10)

# for 
# while not q.full:

# processes = [Process(target=factorial, args=(i,)) for i in range(3)]
# for p in processes:
#     p.start()
# for p in processes:
#     p.join()


# @utils.print_result
# def call_factorial(n):
#     return factorial(n)

# call_factorial(7)


from multiprocessing import Process, Queue
import math
import sys
sys.set_int_max_str_digits(0)

def factorial(n, queue):
    """Calcul CPU-bound — retourne résultat via queue"""
    result = math.factorial(n)
    queue.put((n, result))  # ← stocker dans la queue

# Créer une queue pour communiquer entre processus
q = Queue()

# Données : des grands nombres
numbers = [1000, 5000, 10000]

# Créer les processus
processes = [
    Process(target=factorial, args=(num, q))
    for num in numbers
]

# Démarrer tous les processus
for p in processes:
    p.start()

# Attendre que tous finissent
for p in processes:
    p.join()

# Récupérer les résultats de la queue
results = {}
while not q.empty():
    n, result = q.get()
    results[n] = len(str(result))

print(results)

   
# from multiprocessing import Process

# def worker(name):
#     print(f"Worker {name}")

# processes = [Process(target=worker, args=(i,)) for i in range(3)]
# for p in processes:
#     p.start()
# for p in processes:
#     p.join()