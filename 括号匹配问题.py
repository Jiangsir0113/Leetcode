# -*- coding: utf-8 -*-
# created by Frank Jiang on 2020/8/12 14:29

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return

    def is_empty(self):
        return len(self.stack) == 0


def brace_match(s):
    match = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(brace_match('(){()}{}[]'))
print(brace_match('({[]}}'))
