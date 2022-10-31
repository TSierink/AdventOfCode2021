from sys import setprofile
from turtle import backward
from unittest import case


f = open("input/testday2.txt", "r").read().split('\n')

depth = 0
horizontal = 0
aim = 0

for i in range(0, len(f)):
    step = int(f[i][len(f[i])-1:len(f[i])])
    print(step)
    direction = f[i][:len(f[i])-2]

    match direction:
        case "up":
            aim -= step
        case "down":
            aim += step
        case "forward":
            horizontal += step
            depth += (step*aim)

print(horizontal*depth)
