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
file_path = sys.argv[1]

# Get any optional arguments
optional_arg = ""
if len(sys.argv) == 3:
    optional_arg = sys.argv[2]

if optional_arg == "w":
    # Overwrite file with user input
    with open(file_path,"w") as file:
        file.write(get_input())
else:
    # Read and print contents of file
    file = open(file_path,"a+")
    file.seek(0,0)
    data = file.read()
    print(data)
    if optional_arg == "c":
        # Create a copy of the file, write the current contents then append user input
        file_copy = open(file_path+"copy","w")
        file_copy.write(data)
        file_copy.write(get_input())
        file_copy.close()
    else:
        # Append user input
        file.write(get_input())
    file.close()