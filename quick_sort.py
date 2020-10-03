# -*- coding: utf-8 -*-
# created by Frank Jiang on 2020/8/10 14:05
import random

from Python_code.算法练习.cal_time import *


# @cal_time
def _quick_sort(li, left, right):
    if left < right:  # 至少两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 寻找右边的比tmp大的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 将右边的值写到左边的空位上
        while left < right and li[left] <= tmp:  # 寻找左边的比tmp小的数
            left += 1
        li[right] = li[left]  # 将左边的值写到右边的空位上
    li[left] = tmp
    return left


@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


li = list(range(10000))
random.shuffle(li)
quick_sort(li)
