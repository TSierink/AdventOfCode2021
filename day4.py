def prep(f):
    draws = f[0].split(',')
    _bords = f[1:]
    bords = []
    final_bords = [[]]*len(_bords)

    for b in _bords:
        bords.append(b.split('\n'))

    for i, b in enumerate(bords):

        single_bord = ['']*len(b)

        for j, l in enumerate(b):

            v = l.split(' ')

            while '' in v:
                v.remove('')

            new_line = []

            for w in v:
                new_line.append(int(w))

            single_bord[j] = new_line

        final_bords[i] = single_bord

    return final_bords, draws


def check_bord(b, v):
    for i, l in enumerate(b):
        if int(v) in l:
            return (i, l.index(int(v)))
    return False


def check_horizontal(b):
    if [True, True, True, True, True] in b:
        return True
    else:
        return False


def check_vertical(b):
    for i in range(5):
        if b[0][i] and b[1][i] and b[2][i] and b[3][i] and b[4][i]:
            return True
    return False


def run_through(draws, bords_values, bords_bools):
    for d_value in draws:

        for x, v_bord in enumerate(bords_values):

            if check_bord(v_bord, d_value):
                y, z = check_bord(v_bord, d_value)
                bords_bools[x][y][z] = True

        for i, b_bord in enumerate(bords_bools):

            if check_horizontal(b_bord):
                return (d_value, i, b_bord)

            if check_vertical(b_bord):
                return (d_value, i, b_bord)


def get_sum(winner, values):

    numbers = []

    for i, l in enumerate(winner):
        for j, v in enumerate(l):
            if not v:
                numbers.append(values[i][j])
    return numbers


if __name__ == '__main__':
    file = open("input/day4input.txt", "r").read().split('\n\n')
    bords_values_, draws_ = prep(file)
    bords_bools_ = [[[False] * 5 for _ in range(5)] for _ in range(100)]
    final_number, i, winning_bord = run_through(draws_, bords_values_, bords_bools_)
    numbers = get_sum(winning_bord, bords_values_[i])

    print(sum(numbers)*int(final_number))
