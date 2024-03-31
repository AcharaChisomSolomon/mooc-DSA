import time

n = 10 ** 5
print("n:", n)
numbers = []

start_time1 = time.time()
for i in range(n):
    numbers.append(i + 1)
end_time1 = time.time()

print("additions:")
print("time:", round(end_time1 - start_time1, 2), "s")

start_time2 = time.time()
for i in range(n):
    numbers.pop(0)
end_time2 = time.time()

print("deletions:")
print("time:", round(end_time2 - start_time2, 2), "s")