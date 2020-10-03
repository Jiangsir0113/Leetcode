nums = [3, 5, 6, 9, 8, 4, 0, 1]

count = 0
i = 0
for i in range(len(nums) - 1):
    n = 0
    flag = True
    for n in range(len(nums) - 1 - i):
        count += 1
        if nums[n] > nums[n + 1]:
            flag = False
            nums[n], nums[n + 1] = nums[n + 1], nums[n]
        n += 1
    if flag:
        break
    i += 1
    print(nums)
print(count)
