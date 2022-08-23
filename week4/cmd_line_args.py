# First import the sys library in order to access command line args
import sys

# Command line args can be accessed using sys.argv (this is actually a list of the arguments)
# The first argument is always the path of the running program and is accessed using sys.argv[0]
script_path = sys.argv[0]
print(script_path)

# Let's try taking in another argument to our program, for examle the user's name
user_name = sys.argv[1]

# Let's modify our program to take some options that will let us print the username in uppercase and/or backwards!
# If a user adds -u, let's make the name uppercase and if they add -r, lets return the name backwards

# First create two variables to store potential options
option_1 = ""
option_2 = ""

# Note since these are optional, we will need to check the length of sys.argv before trying to access the third/fourth arguments as they may not exist!
if len(sys.argv) > 2:
    option_1 = sys.argv[2]
if len(sys.argv) == 4:
    option_2 = sys.argv[3]

# Now we can check if the options have been set and apply the relevant functionality
# Note by using or, it doesn't matter which order the options appear in!
if option_1 == "-u" or option_2 == "-u":
    user_name = user_name.upper()
if option_1 == "-r" or option_2 == "-r":
    user_name = user_name[::-1]

# Finally, print the result of the script
print("Hello " + user_name)

# This is just a short introduction, but shows how powerful command line arguments can be when used correctly.