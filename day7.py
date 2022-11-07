
if __name__ == '__main__':
    
    file = open("input/day7input.txt", "r").read().split(',')
    state = [int(f) for f in file]
    
    cost_list = []
    for i in range(max(state)+1):
        diff = [abs(s-i) for s in state]
        #diff = [((d*(d+1))/2) for d in diff]    #UN-COMMENT FOR PART 2
        cost_list.append(sum(diff))
    
    print(min(cost_list))
    
