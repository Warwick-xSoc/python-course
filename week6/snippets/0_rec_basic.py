# Calculates 1 + 2 + ... + n, recursively
def sum_of_first(n: int):
    # Base Case
    if n == 0:
        return 0
    
    # Recursive Step
    return n + sum_of_first(n-1)

print(sum_of_first(4))

# Try 7, 0, -1, 100, 10000
# Replace + with *, Try 4
# Fix?