from random import shuffle

def in_order(some_list):
    for i in range(len(some_list)-1):
        if some_list[i] > some_list[i+1]:
            return False
    return True

def bogosort(some_list):
    while not in_order(some_list):
        shuffle(some_list)

nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1]
bogosort(nums)
print(nums)