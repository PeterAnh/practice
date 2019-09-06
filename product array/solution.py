import os
import string
import random
import time
import timeit

def product_array(arr):
    length = len(arr)
    result = [0] * length
    """
    Naive approach: O(n^2) complexity
    length = len(arr)
    for i in range(length):
        temp = 1;
        for j in range(length):
            if(arr[j] != arr[i]): 
                temp = temp * arr[j]
        result.append(temp)
    """

    left_arr = [None] * length
    right_arr = [None] * length
    left_arr[0] = 1
    right_arr[length-1] = 1
    multi = 1
    for i in range(1,length):
        multi = multi * arr[i-1]
        left_arr[i] = multi
    
    multi = 1
    for i in range(length-2,-1,-1):
        multi = multi * arr[i+1]
        right_arr[i] = multi

    for i in range(0,length):
        result[i] = left_arr[i] * right_arr[i]

    return result
def product_array_naive(arr):
    length = len(arr)
    result = []
    """
    Naive approach: O(n^2) complexity
    """
    length = len(arr)
    for i in range(length):
        temp = 1;
        for j in range(length):
            if(arr[j] != arr[i]): 
                temp = temp * arr[j]
        result.append(temp)
    return result

def big_array(n=100):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,n))
    return arr

def timer(arr,f):
    start_time = timeit.default_timer()
    def run(f):
        f(arr)
        pass
    stop_time = timeit.default_timer()
    return stop_time - start_time

def main():

    arr = list(map(int, input("Enter an array of numbers: ").split()))
    print("Original array: " + str(arr) + "\n")
    print("Product array: " + str(product_array(arr)) + "\n")

    size = int(input("Enter array size: "))

    """
    Test with big array:
    """
    arr = big_array(size)
    """
    print (timer(arr, product_array(arr)) * 10000000, " seconds")
    print (timer(arr, product_array_naive(arr)) * 10000000," seconds")
    """
    print (timeit.timeit(lambda: product_array(arr), number=1))
    print (timeit.timeit(lambda: product_array_naive(arr), number=1))


if __name__ == '__main__':
    main()

