# -*- coding: utf-8 -*-
# created by Frank Jiang on 2020/8/10 13:23

def insert_sort(li):
    for i in range(1, len(li)):  # i表示摸到牌的下标
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)


li = [3, 2, 1, 9, 5, 8, 6, 7, 4]
print(li)
insert_sort(li)
