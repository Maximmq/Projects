f = open('325_26.txt', 'r')
count = int(f.readline())
nums, row, place = [], 0, 0
for i in range(count):
    busy = list(map(int, f.readline().split()))
    busy[1] = -busy[1]
    nums += [busy]
nums.sort()
print(nums)
for i in range(len(nums)):
    if nums[i][0] == nums[i - 1][0] and nums[i][1] - nums[i - 1][1] == 3:
        row = nums[i][0]
        place = - nums[i][1] + 1
print(row, place)
