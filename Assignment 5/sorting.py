from timeit import default_timer as timer
import random


# https://runestone.academy/ns/books/published/pythonds/SortSearch/TheBubbleSort.html
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


'''
https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
The function which implements QuickSort.
arr :- array to be sorted.
start :- starting index of the array.
stop :- ending index of the array.
'''


def quicksort(arr, start, stop):
    if (start < stop):
        # pivotindex is the index where
        # the pivot lies in the array
        pivotindex = partitionrand(arr, start, stop)

        # At this stage the array is
        # partially sorted around the pivot.
        # Separately sorting the
        # left half of the array and the
        # right half of the array.
        quicksort(arr, start, pivotindex - 1)
        quicksort(arr, pivotindex + 1, stop)


# This function generates random pivot,
# swaps the first element with the pivot
# and calls the partition function.
def partitionrand(arr, start, stop):
    # Generating a random number between the
    # starting index of the array and the
    # ending index of the array.
    randpivot = random.randrange(start, stop)

    # Swapping the starting element of
    # the array and the pivot
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)


'''
This function takes the first element as pivot,
places the pivot element at the correct position
in the sorted array. All the elements are re-arranged
according to the pivot, the elements smaller than the
pivot is places on the left and the elements
greater than the pivot is placed to the right of pivot.
'''


def partition(arr, start, stop):
    pivot = start  # pivot

    # a variable to memorize where the
    i = start + 1

    # partition in the array starts from.
    for j in range(start + 1, stop + 1):

        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = \
        arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot


# https://www.programiz.com/dsa/selection-sort
def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


# https://www.programiz.com/dsa/insertion-sort
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


def main():
    # Bubble Sort
    # bubbleSort(list(range(1, 10000)))
    # list(range(1, 1000))

    # Quick Sort
    # array = list(range(1, 200000))

    # quicksort(array, 0, len(array) - 1)

    # Selection Sort
    data = list(range(1, 100000))
    size = len(data)

    start = timer()
    selectionSort(data, size)
    end = timer()
    print(end - start)


    # Insertion Sort
    # data = list(range(1, 100000))
    #
    # start = timer()
    # insertionSort(data)
    # end = timer()
    # print(end - start)


if __name__ == "__main__":
    main()
