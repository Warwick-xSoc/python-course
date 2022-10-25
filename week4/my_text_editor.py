import sys

# Function that gets user input and stores as separate lines
# Returns a string containing all user input separated by \n
def get_input():
    data = ""
    line = input("Input the next line of the file: ")
    while not line == "quit":
        data += line + "\n"
        line = input("Input the next line of the file: ")
    return data

# Get the path of the file to read/write


# Get any optional arguments
optional_arg = ""


if optional_arg == "w":
    # Overwrite file with user input

else:
    # Read and print contents of file

    if optional_arg == "c":
        # Create a copy of the file, write the current contents then append user input

    else:
        # Append user input
