def sort(arr: list) -> list:
    """Merge sort recursive implementation:
    Time complexity O(n log n), Memory O(n), Stable
    """
    if len(arr) <= 1:
        return arr

    middle = int(len(arr) / 2)
    left = sort(arr[:middle])
    right = sort(arr[middle:])
    return merge(left, right)


def merge(left_arr: list, right_arr: list) -> list:
    result = []
    li, ri = 0, 0
    while li < len(left_arr) and ri < len(right_arr):
        if left_arr[li] <= right_arr[ri]:
            result.append(left_arr[li])
            li += 1
        else:
            result.append(right_arr[ri])
            ri += 1

    result.extend(left_arr[li:])
    result.extend(right_arr[ri:])
    return result
