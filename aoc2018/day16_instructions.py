def addr(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = r[a] + r[b]

    return tuple(ret)


def addi(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = r[a] + b

    return tuple(ret)


def mulr(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = r[a] * r[b]

    return tuple(ret)


def muli(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = r[a] * b

    return tuple(ret)


def banr(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = r[a] & r[b]

    return tuple(ret)


def bani(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = r[a] & b

    return tuple(ret)


def borr(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = r[a] | r[b]

    return tuple(ret)


def bori(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = r[a] | b

    return tuple(ret)


def setr(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = r[a]

    return tuple(ret)


def seti(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = a

    return tuple(ret)


def gtir(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = int(a > r[b])

    return tuple(ret)


def gtri(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = int(r[a] > b)

    return tuple(ret)


def gtrr(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = int(r[a] > r[b])

    return tuple(ret)


def eqir(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = int(a == r[b])

    return tuple(ret)


def eqri(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = int(r[a] == b)

    return tuple(ret)


def eqrr(r, a, b, c):
    ret = [r[0], r[1], r[2], r[3]]
    ret[c] = int(r[a] == r[b])

    return tuple(ret)
