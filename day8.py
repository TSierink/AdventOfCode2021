'''
1: 2 segments
4: 4 segments
7: 3 segments
8: 7 segments
'''

file = open("input/day8input.txt", "r").read().split('\n')

file = [f[(f.find('|')+2):].split(' ') for f in file]
file_copy = [len(i) for f in file for i in f]

print(file_copy.count(2)+file_copy.count(4)+file_copy.count(3)+file_copy.count(7))