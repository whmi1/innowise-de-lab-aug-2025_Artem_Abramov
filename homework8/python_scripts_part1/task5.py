nums = [2, 7, 11, 15]
target = 9
nums_map = {}
result = []

for i in range(len(nums)):
    difference = target - nums[i]
    if difference in nums_map:
        result = [nums_map[difference], i]
        break
    nums_map[nums[i]] = i    

print(f'nums = {nums}\ntarget = {target}')

if not result:
    print("Таких чисел нет в списке.")
else:
    print(f'Ответ: {result}')
