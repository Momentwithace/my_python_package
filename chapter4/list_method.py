rng = list(range(1, 100, 5))
print(rng)

rng.append(3000)
print(rng)

rng.append([2, 1, 4])
print(rng)

rng.extend([2, 3, 4])
print(rng)


rng.insert(0, 23)
print(rng)

rng.count(0)
print(rng)

popped = rng.pop()
print(popped)
print(rng)

popped = rng.pop(2)
print(popped)
print(rng)

rng.remove(1)
print(rng)


idx = rng.index(51)
print(idx)
print(rng)

lst = rng.copy()

rng.clear()

print(rng)
print(lst)