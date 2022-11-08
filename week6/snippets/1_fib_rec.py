def fib(n: int) -> int:
    if n < 0:
        raise ValueError("Not Defined")
    if n == 0 or n == 1:
        return n
    
    return fib(n-1) + fib(n-2)

print(fib(4))
print(fib(20))
print(fib(50))  # Why?