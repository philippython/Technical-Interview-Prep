from time import perf_counter
from threading import Thread

COUNT = 50_000_000

def countdown(n):
    while n>0:
        n -= 1

start = perf_counter()
countdown(COUNT)
end = perf_counter()

print('Time taken in seconds -', f"{end - start: 0.2f}")