'''
1: 2 segments
4: 4 segments
7: 3 segments
8: 7 segments

0 ABCEFG
1 CF
2 ACDEG
3 ACDFG
4 BCDF
5 ABDFG
6 ABDEFG
7 ACF
8 ABCDEFG
9 ABCDFG
'''


def find_9(values, clue):
    for v in values:
        if len(v) == 6 and (set(clue).issubset(set(v))):
            return v


def find_0(values, clue):
    for v in values:
        if len(v) == 6 and (set(clue[0]) | set(clue[1])).issubset(set(v)) and (set(clue[2]).issubset(set(v))):
            return v


def find_2(values, clue):
    for v in values:
        if len(v) == 5 and set(clue).issubset(set(v)):
            return v


def find_5(values, clue):
    for v in values:
        if len(v) == 5 and set(clue).issubset(set(v)):
            return v


def find_3(values, clue):
    for v in values:
        if len(v) == 5 and v != clue[0] and v != clue[1]:
            return v


def find_6(values, clue):
    for v in values:
        if len(v) == 6 and v != clue[0] and v != clue[1]:
            return v


def prep():
    file = open("input/day8input.txt", "r").read().split('\n')

    file_numbers_ = [f[:(f.find('|')-1)].split(' ') for f in file]
    file_numbers_ = [[sorted(i) for i in f] for f in file_numbers_]
    file_numbers_len_ = [[len(i) for i in f] for f in file_numbers_]

    file_display_ = [f[(f.find('|')+2):].split(' ') for f in file]
    file_display_ = [[sorted(i) for i in f] for f in file_display_]

    return file_numbers_, file_numbers_len_, file_display_


if __name__ == '__main__':

    file_numbers, file_numbers_len, file_display = prep()

    found = [[None for _ in range(10)] for _ in range(200)]

    for x, (i, j) in enumerate(zip(file_numbers, file_numbers_len)):
        for k, l in zip(i, j):

            if l == 2:
                found[x][1] = k
            if l == 3:
                found[x][7] = k
            if l == 4:
                found[x][4] = k
            if l == 7:
                found[x][8] = k

    for f, n in zip(found, file_numbers):
        a = list(set(f[7]) - (set(f[7]) & set(f[1])))

        almost_9 = f[4]+a

        f[9] = find_9(n, almost_9)

        g = list(set(f[9]) - set(f[4]) - set(a))

        e = list(set(f[8])-set(f[9]))

        f[0] = find_0(n, (e, g, f[7]))

        print(f[8], f[0])

        d = list(set(f[8])-set(f[0]))

        f[2] = find_2(n, e)

        b = list((set(f[4]) - set(f[1])) - set(d))

        f[5] = find_5(n, b)

        f[3] = find_3(n, (f[5], f[2]))

        f[6] = find_6(n, (f[9], f[0]))

    actual_list = []
    for f, display_ in zip(found, file_display):
        actual = []
        for display in display_:

            actual += str(f.index(display))

        actual_list.append(actual)

    actual_list = [''.join(v) for v in actual_list]
    actual_list = [int(v) for v in actual_list]
    print(sum(actual_list))
