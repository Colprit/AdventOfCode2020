input = [1,20,8,12,0,14]

N = 30000000

spoken = {i: input.index(i) for i in input[:-1]}
next = input[-1]

i = len(input)-1
while i < N-1:
    k = i - spoken.get(next,i)
    spoken.update({ next : i })
    next = k
    i += 1

print(next)
