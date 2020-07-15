### 交换
# 冒泡
def sort_bubble(nums):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


def quick(arr, left=None, right=None):
    left = 0
    right = len(arr) - 1
    if left < right:
        partition_index = partition(arr, left, right)
        quick(arr, left, partition_index - 1)
        quick(arr, partition_index + 1, right)
    return arr


def swap(arr, i, index):
    arr[i], arr[index] = arr[index], arr[i]


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1

    swap(arr, pivot, index - 1)
    return index - 1


import numpy as np

nums = np.random.randint(0, 100, 20)
print("源数据:", nums)
# print("新数据:", sort_bubble(nums))
print("新数据:", quick(nums))
