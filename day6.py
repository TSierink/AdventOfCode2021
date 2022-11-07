DAYS = 256 # CHANGE TO 80 FOR PART 1

if __name__ == '__main__':
    file = open("input/day6input.txt", "r").read().split(',')
    state = [int(f) for f in file]
    
    # print(state)
    # state = [3,4,3,1,2]
    
    state_dict = {}
    for i in range(9):
        state_dict[f"{i}"] = state.count(i)
    
    print(state_dict)
    
    for i in range(DAYS):
        print(i)
        temp_0 = state_dict.get("0")
        
        state_dict["0"] = state_dict.get("1")
        state_dict["1"] = state_dict.get("2")
        state_dict["2"] = state_dict.get("3")
        state_dict["3"] = state_dict.get("4")
        state_dict["4"] = state_dict.get("5")
        state_dict["5"] = state_dict.get("6")
        state_dict["6"] = temp_0 +state_dict.get("7")
        state_dict["7"] = state_dict.get("8")
        state_dict["8"] = temp_0
               
        
    print(sum(state_dict.values()))   