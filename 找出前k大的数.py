# -*- coding: utf-8 -*-
# created by Frank Jiang on 2020/8/11 14:52
import random


# 1.冒泡排序实现
def bubble_sort(li, k):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return li[:k]


li = list(range(100))

random.shuffle(li)

print(bubble_sort(li, 10))
