import random

array = [random.randint(0,100) for i in range(100)]


def bubbleSort(arr):
    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True

        if swapped == False:
            break
    return arr

print(bubbleSort(array)==sorted(array))