def fib_linear(n: int) -> int:
    if n < 0:
        raise ValueError("Not Defined")
    if n in [0, 1]:
        return n
    
    prev = 0
    curr = 1
    for _ in range(n-1):
        new = prev + curr
        prev = curr
        curr = new
    return curr

print(fib_linear(50))
print(fib_linear(100))