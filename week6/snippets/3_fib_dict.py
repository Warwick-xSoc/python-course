seen = {}

def fib_dict(n: int) -> int:
    if n <= 1:
        return n
    
    # Lookup or recurse
    prev1 = seen[n-1] if n-1 in seen else fib_dict(n-1)
    prev2 = seen[n-2] if n-2 in seen else fib_dict(n-2)

    # Add to lookup when found
    seen[n] = prev1 + prev2
    return seen[n]

print(fib_dict(50))
print(fib_dict(100))