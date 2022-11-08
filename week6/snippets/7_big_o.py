# The size of nums affects the time things take to run.
nums = [75, -63, 39, -88, 83, -7, 12, -99, 83, 29, -43, -33, -74, -76, -21, -100, 26, 97, 37, -61]
target = 14
found = False

# Determines if any two distinct numbers in the list add up to the target
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target and i != j:
            found = True

print(":)") if found else print(":(")

# In this case, len(nums) = 20. The inner loop executes 20^2 = 400 times.
# Is this a good algorithm?