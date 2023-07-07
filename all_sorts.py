def bubble_sort(array: list) -> list:
    for i in range(len(array)-1):
        for j in range((len(array)-1)- i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j+1], array[j]
    return array

def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array

def selection_sort(array: list) -> list :
    for i in range(0, len(array) - 1):
        low = i
        for j in range(i + 1, len(array)):
            if array[j] < array[low]:
                low = j
    array[i], array[low] = array[low], array[i]
    return array
