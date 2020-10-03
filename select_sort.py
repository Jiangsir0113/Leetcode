# -*- coding: utf-8 -*-
# created by Frank Jiang on 2020/8/9 17:29

def select_sort(li):
    for i in range(len(li) - 1):  # 第i趟
        min_loc = i  # 最小数的下标
        for j in range(i + 1, len(li)):  # for循环无序区寻找最小数的下标
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


li = [2, 5, 4, 1, 8, 3, 6, 9, 7]
print(li)
select_sort(li)
