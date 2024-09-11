def avg(*args: int) -> float:
    return sum(args) / len(args)

print(avg(1, 2, 3))
print(avg(10, 20 , 30, 40))
print(avg(2.2, 2.4, 2.6))