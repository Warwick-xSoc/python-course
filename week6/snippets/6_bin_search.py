def find(items, target) -> bool:
    return search(items, target, 0, len(items) - 1)

def search(items, target, low, high) -> bool:
    if low > high:  # Guessed everywhere possible
        return False
    
    mid = (low + high) // 2  # Make a guess in the middle
    
    if items[mid] > target:  # Guess too high
        return search(items, target, low, mid - 1)
    elif items[mid] < target:   # Guess too low
        return search(items, target, mid + 1, high)
    else:  # Got it!
        return True

# Only works on lists in order (in this case, alphabetical).
fruits = ["Apple", "Banana", "Cherry", "Durian", "Fig", "Grapefruit", "Orange", "Peach", "Pear", "Pineapple"]

print(find(fruits, "Pear"))
print(find(fruits, "Chocolate"))
print(find(fruits, "Z"))