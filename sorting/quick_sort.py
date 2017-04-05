def sort(arr: list) -> list:
    """Quick sort in-place recursive implementation
    from "Problem Solving with Algorithms and Data Structures Using Python"
    Time complexity O(n log n), Memory O(1), Unstable
    """
    quickSortHelper(arr, 0, len(arr) - 1)
    return arr  # not necessarily because in-place


def quickSortHelper(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)

        quickSortHelper(arr, first, splitpoint - 1)
        quickSortHelper(arr, splitpoint + 1, last)


def partition(arr, first, last):
    pivotvalue = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark
