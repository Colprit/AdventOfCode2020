with open('day09_input.txt') as f:
  data = f.read()

nums = data.split('\n')
nums = [int(n) for n in nums]

x = 20874512

for i in range(len(nums)):
  total = 0
  j = i
  while total < x:
    total += nums[j]
    j += 1
  if total == x:
    print('found')
    break

cont = nums[i:j]
print( max(cont) + min(cont) )