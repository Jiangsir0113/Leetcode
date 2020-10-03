nums = [i for i in range(1, 10)]
miss_nums = [1, 2, 3, 4, 5, 6, 0, 8, 9]
print([x for x in miss_nums])
for s in nums:
    for r in miss_nums:
        print(s ^ r)
