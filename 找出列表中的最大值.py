nums = [3, 5, 6, 9, 8, 4, 0, 1, 2, 7]

n = 0
for i in nums:
    if n < i:
        n = i
print(n, nums.index(n))
