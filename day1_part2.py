f = open("input/day1input.txt", "r").read().split('\n')

for l in f:
    l = int(l)

count = 0
prev = 9999
now = -9999

for i in range(2,len(f)):
    now = int(f[i-2])+int(f[i-1])+int(f[i])
    if now>prev:
        count+=1
    prev = now

print(count)