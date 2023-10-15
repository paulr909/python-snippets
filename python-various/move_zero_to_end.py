nums = [1, 0, 4, 3, 6, 0, 2, 5, 7]

for num in nums:
    if num == 0:
        nums.remove(num)
        nums.append(num)

print(nums)
