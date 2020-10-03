# -*- coding: utf-8 -*-
# created by Frank Jiang on 2020/8/12 15:26
from collections import deque


# q = deque([1,2,3,4,5],5)
# q.append(6)  # 队尾进队
# print(q.popleft())  # 队首出队
# #  用于双向队列
# q.appendleft(1)  # 队首进队
# q.pop()  # 队尾出队

# Linux中的tail命令
def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q


print(tail(5))
for line in tail(5):
    print(line, end='')
