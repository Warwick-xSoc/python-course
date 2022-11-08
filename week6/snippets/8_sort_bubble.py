
def in_order(some_list):
    for i in range(len(some_list)-1):
        if some_list[i] > some_list[i+1]:
            return False
    return True

def bubble(some_list):
    flag = False
    while not flag:
        flag = True
        for i in range(len(some_list) - 1):
            # Not in order
            if some_list[i] > some_list[i+1]:
                flag = False
                # Swap the two elements
                temp = some_list[i]
                some_list[i] = some_list[i+1]
                some_list[i+1] = temp

nums = [2, 3, 4, 10, 6, 1, 8, 9, 5, 11, 12, 7]
bubble(nums)
print(nums)