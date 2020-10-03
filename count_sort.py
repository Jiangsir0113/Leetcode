# -*- coding: utf-8 -*-
# created by Frank Jiang on 2020/8/11 16:50
import random


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)
    return li


li = [random.randint(0, 100) for _ in range(1000)]
print(count_sort(li))
