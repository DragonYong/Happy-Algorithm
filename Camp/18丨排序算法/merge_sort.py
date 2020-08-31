import numpy as np


def merge_sort(arr):
    # 判断数据长度小于2的情况
    if len(arr) < 2:
        return arr
    middle = len(arr)//2
    # print(middle)
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


arr = np.random.randint(0, 100, 20)
print("原始数据:", arr)
print(list(arr))
print("排序数据:", merge_sort(list(arr)))
