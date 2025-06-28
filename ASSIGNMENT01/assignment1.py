import random
import time


def bubble_sort(my_list):
    n = len(my_list)
    steps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            steps +=1# 1 for comparison
            if my_list[j] > my_list[j + 1]:
                steps += 3#3 for swap
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return steps

def selection_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        min_idx = i  # record the index of the smallest value,
                     # initialized with where the smallest value may be found
        for j in range(i + 1, n):              # go through list,
            steps += 1# 1 for comparison
            if my_list[j] < my_list[min_idx]:  # and every time we find a smaller value,
                min_idx = j                    # record its index (note how nothing has moved at this point.)
                

        steps += 1# 1 for comparison
        if min_idx != i:
            steps += 3# 3 for swap
            my_list[min_idx], my_list[i] = my_list[i], my_list[min_idx]
    return steps


def insertion_sort(my_list):
    steps = 0
    for i in range(1, len(my_list)):
        curr = my_list[i]  # store the first number in the unsorted part of array into curr
        steps += 1# 1 for swap
        j = i
        while j > 0 and my_list[j - 1] > curr:       # this loop shifts value within sorted part of array
            steps += 2# 1 for comparison 1 for swap
            my_list[j] = my_list[j - 1]              # to open a spot for curr
            j -= 1
        my_list[j] = curr
        steps += 1# 1 for swap
    return steps



def partial_sort(my_list, left, right):
    steps = 0
    # Ensure the indices are within bounds
    if left < 0 or right >= len(my_list):
        raise ValueError("Indices are out of bounds")
    
    for i in range(left + 1, right + 1):  # Start from left + 1 since the element at 'left' is already considered sorted
        curr = my_list[i]  # Store the current value in the unsorted part
        steps += 1# 1 for swap
        j = i
        while j > left and my_list[j - 1] > curr:  # Move elements within the sorted part
            my_list[j] = my_list[j - 1]
            steps += 2# 1 for comparison 1 for swap
            j -= 1
        my_list[j] = curr
        steps += 1# 1 for swap
    return steps

def quick_sort(mylist):
    steps = 0
    steps = recursive_quick_sort(mylist, 0, len(mylist) - 1, steps)
    return steps

def recursive_quick_sort(mylist, left, right, steps, THRESHOLD=32):
    if right - left <= THRESHOLD:
        steps = quick_insertionsort(mylist, left, right, steps)
    else:
        pivot_position, steps = partition(mylist, left, right, steps)
        steps = recursive_quick_sort(mylist, left, pivot_position - 1, steps)
        steps = recursive_quick_sort(mylist, pivot_position + 1, right, steps)
    return steps

def partition(mylist, left, right, steps):
    pivot_location = random.randint(left, right)
    pivot = mylist[pivot_location]

    # Swap pivot with right
    mylist[pivot_location], mylist[right] = mylist[right], mylist[pivot_location]
    steps += 3  # 3 for swap

    end_of_smaller = left - 1

    for j in range(left, right):
        steps += 1  # 1 for comparison
        if mylist[j] <= pivot:
            end_of_smaller += 1
            mylist[end_of_smaller], mylist[j] = mylist[j], mylist[end_of_smaller]
            steps += 3  # 3 for swap

    # Restore pivot
    mylist[end_of_smaller + 1], mylist[right] = mylist[right], mylist[end_of_smaller + 1]
    steps += 3  # 3 for swap

    return end_of_smaller + 1, steps

def quick_insertionsort(my_list, left, right, steps=0):
    if left < 0 or right >= len(my_list):
        raise ValueError("Indices are out of bounds")
    
    for i in range(left + 1, right + 1):
        curr = my_list[i]
        steps += 1  # 1 for swap
        j = i
        while j > left and my_list[j - 1] > curr:
            my_list[j] = my_list[j - 1]
            steps += 2  # 1 for comparison 1 for swap
            j -= 1
        my_list[j] = curr
        steps += 1  # 1 for swap
    return steps

def create_list(listSize, sort_func, left=None, right=None):
    rand_list = [random.randint(0, 100) for val in range(listSize)]
    rand_list.sort(reverse=True)

    start_time = time.perf_counter()

    if left is not None and right is not None:
        steps = sort_func(rand_list, left, right)
    else:
        steps = sort_func(rand_list)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print("steps needed for sorting: {}".format(steps))
    print("Sort used: {}".format(sort_func.__name__))
    print("Time taken: {:.6f} seconds".format(elapsed_time))

def best_case(listSize, sort_func, left=None, right=None):
    rand_list = [random.randint(0, 100) for val in range(listSize)]
    rand_list.sort(reverse=False)

    start_time = time.perf_counter()

    if left is not None and right is not None:
        steps = sort_func(rand_list, left, right)
    else:
        steps = sort_func(rand_list)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print("steps needed for sorting: {}".format(steps))
    print("Sort used: {}".format(sort_func.__name__))
    print("Time taken: {:.6f} seconds".format(elapsed_time))

def average_case(listSize, sort_func, left=None, right=None):
    rand_list = [random.randint(0, 100) for val in range(listSize)]

    start_time = time.perf_counter()

    if left is not None and right is not None:
        steps = sort_func(rand_list, left, right)
    else:
        steps = sort_func(rand_list)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print("steps needed for sorting: {}".format(steps))
    print("Sort used: {}".format(sort_func.__name__))
    print("Time taken: {:.6f} seconds".format(elapsed_time))
    


def repeat_list(n, sort_type, left=None, right=None):
    while n < 40961:
        if left is not None and right is not None:
            right = n // 2  # sort first half of list
        create_list(n, sort_type, left, right)
        n *= 2


        
def main():
    best_case(100, bubble_sort)
    best_case(100, selection_sort)
    best_case(100, insertion_sort)
    best_case(100, partial_sort, 0, 50)
    best_case(100, quick_sort)
    average_case(100, bubble_sort)
    average_case(100, selection_sort)
    average_case(100, insertion_sort)
    average_case(100, partial_sort, 0, 50)
    average_case(100, quick_sort)
    repeat_list(10, bubble_sort)
    repeat_list(10, selection_sort)
    repeat_list(10, insertion_sort)
    repeat_list(10, partial_sort, 1, 5)
    repeat_list(10, quick_sort)

main()