def prep(file_):
    file_ = [f.replace(' -> ', ',') for f in file_]
    print(len(file_))
    file_ = [f.split(',') for f in file_]

    x1 = []
    x2 = []
    y1 = []
    y2 = []

    for l in file_:
        x1.append(int(l[0]))
        y1.append(int(l[1]))
        x2.append(int(l[2]))
        y2.append(int(l[3]))

    return x1, y1, x2, y2


def filter_diagonal(x1, y1, x2, y2):
    removelist = []
    for x1_, y1_, x2_, y2_ in zip(x1, y1, x2, y2):
        if (x1_ != x2_) and (y1_ != y2_):
            removelist.append([x1_, y1_, x2_, y2_])

    zpd = list(zip(x1, y1, x2, y2))
    for r in removelist:
        zpd.remove(tuple(r))

    (x1, y1, x2, y2) = zip(*zpd)

    return x1, y1, x2, y2


if __name__ == '__main__':
    file = open("input/day5input.txt", "r").read().split('\n')

    x1, y1, x2, y2 = prep(file)
    zipd = list(zip(x1, y1, x2, y2))
    x1, y1, x2, y2 = filter_diagonal(x1, y1, x2, y2)
    zipd = list(zip(x1, y1, x2, y2))

    count_list = [[0 for _ in range(1000)] for _ in range(1000)]

    for x1_, y1_, x2_, y2_ in zip(x1, y1, x2, y2):
        if (x1_ == x2_):
            if y1_ > y2_:
                y1_, y2_, = y2_, y1_
            for i in range(y1_, y2_+1):
                count_list[x1_][i] += 1
        if (y1_ == y2_):
            if x1_ > x2_:
                x1_, x2_, = x2_, x1_
            for i in range(x1_, x2_+1):
                count_list[i][y1_] += 1

    total = sum(i >= 2 for c in count_list for i in c)
    print(total)
