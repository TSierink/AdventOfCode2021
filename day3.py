# GAMMA - MOST COMMON BIT[i] = bit
# EPISOLON - LEAST COMMON BIT

#ANSWER: MULTIPLY


lines = open("input/day3input.txt", "r").read().split('\n')

totals = [0]*12
gamma = [0]*12
epsilon = [0]*12

for line in lines:
    for i, b in enumerate(line):
        totals[i] += int(b)

for i, t in enumerate(totals):
    gamma[i] = 1 if t>500 else 0
    epsilon[i] = 0 if t>500 else 1

gammaString = ''.join([str(elem) for elem in gamma])
epsilonString = ''.join([str(elem) for elem in epsilon])

print(int(gammaString,2), int(epsilonString,2))
print(int(gammaString,2) * int(epsilonString,2))