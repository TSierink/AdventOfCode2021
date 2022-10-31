f = open("input/day1input.txt", "r").read().split('\n')

count = 0
for i in range(1,len(f)):
    if f[i-1] < f[i]:
        print(f[i-1], f[i], f[i-1] < f[i])
        count+=1

print(count)