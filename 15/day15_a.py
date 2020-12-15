input = [1,3,2] #  1
input = [2,1,3] # 10
input = [1,20,8,12,0,14]

spoken = input

while len(spoken) < 2020:
    last = spoken[-1]
    try:
        last_spoken = spoken[-2::-1].index(last) + 1
    except ValueError:
        last_spoken = 0
    spoken.append(last_spoken)

print(spoken[-1])
