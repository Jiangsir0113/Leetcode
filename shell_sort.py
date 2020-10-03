# -*- coding: utf-8 -*-
# created by Frank Jiang on 2020/8/11 16:32
import random


def shell_sort(li, d):
    while d >= 1:
        for i in range(d, len(li)):
            tmp = li[i]
            j = i - d
            while j >= 0 and li[j] > tmp:
                li[j + d] = li[j]
                j -= d
            li[j + d] = tmp
        d //= 2


li = list(range(100))
random.shuffle(li)
print(li)
shell_sort(li, len(li) // 2)
print(li)
