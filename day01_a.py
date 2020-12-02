with open('day01_input.txt', 'r') as file:
    input = file.read()

nums = input.split()

nums = [int(n) for n in nums]

def findSumTo2020(nums):
  N = len(nums)
  for i in range(N):
    I = nums[i]
    for j in range(i+1,N):
      J = nums[j]
      if I+J == 2020:
        return I, J
  return 0, 0

a,b = findSumTo2020(nums)

print(a,b)
print(a*b)