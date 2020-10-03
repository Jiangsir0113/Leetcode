# nums = [3, 5, 6, 9, 8, 4, 0, 1, 2, 7]
#
# i = 0
# for i in range(len(nums) - 1):
#     i += 1
#     n = 0
#     for n in range(len(nums) - 1):
#         if nums[n] > nums[n + 1]:
#             nums[n], nums[n + 1] = nums[n + 1], nums[n]
#             n += 1
#     print(nums)
import random
from Python_code.算法练习.cal_time import *


@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):  # 第i趟
        exchange = False
        for j in range(len(li) - i - 1):  # 指针
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return


li = list(range(100))

random.shuffle(li)

bubble_sort(li)
print(li)
