with open('day09_input.txt') as f:
  data = f.read()

nums = data.split('\n')
nums = [int(n) for n in nums]

preamble_len = 25


def sum_in(x, Y):
  for i in range(len(Y)):
    for j in range(i+1, len(Y)):
      if Y[i] + Y[j] == x:
        return True
  return False

i = 0
while i < len(nums) - preamble_len:
  if not sum_in(nums[i+25], nums[i:i+25]):
    break
  i += 1

print(nums[i+25])