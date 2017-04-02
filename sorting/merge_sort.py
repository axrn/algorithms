def sort(arr: list) -> list:
    """Bubble sort with small optimizations:
    Time complexity O(n**2), Memory O(1), Stable
    """
    L = len(arr)
    for i in range(L):
        swapped = False
        for j in range(1, L - i):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swapped = True
        if not swapped:
            break
    return arr[-1]
