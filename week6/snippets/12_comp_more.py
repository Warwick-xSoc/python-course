# Even numbers from 1 to 50
even_50 = [num for num in range(1, 51, 2)]
print(even_50)

# Combining the first character of each word into a string
compliments = ["Crazy", "Ostentacious", "Marvelous", "Perfect", "Unbelievable", "Treasured", "Incredible", "Noble", "Grand"]
secret_word = "".join([word[0] for word in compliments])
print(secret_word)

# Nested list comprehensions to form times tables
times_tables = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(times_tables)