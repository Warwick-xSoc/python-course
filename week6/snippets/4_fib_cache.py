from functools import cache

@cache
def fib_cache(n: int) -> int:
    if n <= 1:
        return n
    return fib_cache(n-1) + fib_cache(n-2)

print(fib_cache(50))
print(fib_cache(100))