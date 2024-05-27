'''
Организация купила для своих сотрудников все места в нескольких подряд идущих рядах на концертной площадке. Известно, какие места уже распределены между сотрудниками. Найдите ряд с наибольшим номером, в котором есть два соседних места, таких что слева и справа от них в том же ряду места уже распределены (заняты). Гарантируется, что есть хотя бы один ряд, удовлетворяющий условию. В ответе запишите два целых числа: номер рядя и наименьший номер места из найденных в этом ряду подходящих пар.
'''
f = open('325_26.txt', 'r')
count = int(f.readline())
nums, row, seat = [], 0, 0
for i in range(count):
    taken = list(map(int, f.readline().split()))
    taken[1] = -taken[1]
    nums += [taken]
nums.sort()
print(nums)
for i in range(len(nums)):
    if nums[i][0] == nums[i - 1][0] and nums[i][1] - nums[i - 1][1] == 3:
        row = nums[i][0]
        seat = -nums[i][1] + 1
print('\n', row, seat)
