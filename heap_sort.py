# -*- coding: utf-8 -*-
# created by Frank Jiang on 2020/8/11 9:21
import random
import heapq


def sift(li, low, high):
    """
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:

    sift时间复杂度：O(logn)
    """
    i = low
    j = 2 * i + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子有并且比左孩子大
            j = j + 1  # j指向右孩子
        if li[j] > tmp:  # 如果j位置的值大于堆顶元素
            li[i] = li[j]  # 将j位置的值赋给i位置
            i = j  # 往下看一层
            j = 2 * i + 1  # 下一层的孩子
        else:  # tmp更大，把tmp放到i的位置上
            li[i] = tmp  # 把tmp放到某一级领导位置上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def heap_sort(li):
    """

    :param li: 待排序的列表
    :return:


    heap_sort时间复杂度：
    """
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        # i表示建堆的时候调整的部分的根的下标
        sift(li, i, n - 1)
        # 建堆完成
    for i in range(n - 1, 0, -1):
        # i 指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)


# li = [i for i in range(100)]
# random.shuffle(li)
# print(li)
# heap_sort(li)
# print(li)

# 内置函数heapq使用
"""
li = list(range(100))
random.shuffle(li)
print(li)
heapq.heapify(li)
print(li)
lst = []
for i in range(len(li)):
    lst.append(heapq.heappop(li))
print(lst)

"""
