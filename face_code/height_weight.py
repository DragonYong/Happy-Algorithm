# -*- coding: utf-8 -*-
# @Time     : 2020/8/26-19:48
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : height_weight.py
# @Project  : Happy-Algorithm




def first():
    times = int(input())
    height = input().split()
    weight = input().split()

    heights = [int(i) for i in height]
    weights = [int(i) for i in weight]

    # data_dict = {}
    # for i in range(times):
    #     data_dict[i] = [heights[i], weights[i]]
    # sorted(data_dict[:][0])
    # sorted(data_dict[:][1])
    #
    # print(data_dict)
    # for key,value in data_dict.items():
    #     print(value)
    data_list = [[i + 1, heights[i], weights[i]] for i in range(times)]
    # print(data_list)
    sor = lambda x: x[0]
    sor(data_list)
    print(data_list)


def second():
    length = int(input())
    nums = input()
    nums = [int(i) for i in nums.split()]
    while len(nums) > 1 and len(nums) == length:
        max_num = max(nums)
        min_num = min(nums)
        nums.remove(max_num)
        nums.remove(min_num)
        temp = abs(max_num - min_num)
        nums.append(temp)
    if len(nums) == 1:
        return nums[0]
    else:
        return 0


def threed():
    pass


if __name__ == '__main__':
    # first()
    # second()
    threed()
