# Read lines
lines_oxy = open("input/day3input.txt", "r").read().split('\n')
lines_co2 = open("input/day3input.txt", "r").read().split('\n')

# Check common bit in given position, taking account 
def check_common(bits,position, oxy):
    total = 0
    for b in bits:
        total += int(b[position])

    if oxy:
        common = 1 if total >= (len(bits)/2) else 0
    else:
        common = 0 if total >= (len(bits)/2) else 1
    
    return common


def find(originalRatingList, ratingList, ratingBool):
    
    pos = 0   

    while len(ratingList) > 1:
        
        c = check_common(ratingList,pos, ratingBool)

        for line in originalRatingList:
            if (int(line[pos]) == c) and line in ratingList:
                ratingList.remove(line)

        pos+=1
    return ratingList

print(int(find(lines_oxy, lines_oxy.copy(), True)[0],2)*int(find(lines_co2, lines_co2.copy(), False)[0],2))
