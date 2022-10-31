from sys import setprofile
from turtle import backward
from unittest import case


f = open("input/day2input.txt", "r").read().split('\n')

depth = 0
horizontal=0

for i in range(0,len(f)):
    step = int(f[i][len(f[i])-1:len(f[i])])
    print(step)
    direction = f[i][:len(f[i])-2] 
    
    match direction:
        case "up":
            depth-=step
        case "down": 
            depth+=step
        case "forward":
            horizontal+=step
        case "backward":
            horizontal-=step

print(horizontal*depth)