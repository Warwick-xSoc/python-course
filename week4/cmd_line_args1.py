import sys

print(sys.argv)

name = sys.argv[1]

if len(sys.argv) > 2:
    if sys.argv[2] == "-u":
        name = name.upper()

print("Hello " + name)