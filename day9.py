file = open("input/day9testinput.txt", "r").read().split('\n')

lowPoints=[]

for r_index, r in enumerate(file):
    for c_index, c in enumerate(r):
        
        check = int(file[r_index][c_index])
        
        check_list = []
        
        if r_index != 0:
            check_list.append(int(file[r_index-1][c_index]))
        
        if r_index != len(file)-1:
            check_list.append(int(file[r_index+1][c_index]))
        
        if c_index != 0:
            check_list.append(int(file[r_index][c_index-1]))
        
        if c_index != len(r)-1:
           check_list.append(int(file[r_index][c_index+1]))
           
        if sum([check < c for c in check_list]) == len(check_list):
            lowPoints.append(check+1)

print(sum(lowPoints))