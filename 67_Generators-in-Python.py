def generator():
    for i in range(5):
        yield i

print(next(generator()))
aman = generator()
print(next(aman))
print(next(aman))
print(next(aman))
print(next(aman))
print(next(aman))
print(next(aman))
print(next(aman))