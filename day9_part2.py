import sys
file = open("input/day9input.txt", "r").read().split('\n')

def recurse(x, y, doneList, todo,low):

    if y > 0 and int(file[x][y-1]) != 9:
            todo.append([x, y-1])
                     
    if y < len(file[x])-1 and int(file[x][y+1]) != 9:
            todo.append([x, y+1])
                  
    if x > 0 and (x-1, y) and int(file[x-1][y]) != 9:
            todo.append([x-1, y])
             
    if x < len(file)-1 and int(file[x+1][y]) != 9:
            todo.append([x+1, y])
                
    while len(todo) != 0:
        x_ = todo[0][0]
        y_ = todo[0][1]
        todo.pop(0)
        
        if (x_,y_) not in doneList:
            doneList.append((x_,y_))
            return 1+ recurse(x_, y_, doneList,todo,low)

    return 1


basinSizes = []

for r_index, r in enumerate(file):
    for c_index, c in enumerate(r):

        check = int(file[r_index][c_index])

        check_list = []

        if r_index > 0:
            check_list.append(int(file[r_index-1][c_index]))

        if r_index < len(file)-1:
            check_list.append(int(file[r_index+1][c_index]))

        if c_index > 0:
            check_list.append(int(file[r_index][c_index-1]))

        if c_index < len(r)-1:
            check_list.append(int(file[r_index][c_index+1]))

        if sum([check < c for c in check_list]) == len(check_list):
            basinSizes.append(recurse(r_index, c_index,  [(r_index, c_index)], [],(r_index, c_index)))

basinSizes.sort()
print(basinSizes)
