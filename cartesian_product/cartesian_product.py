def cartesian_product(*lists):
    ret = [[x] for x in lists[0]]
    if len(lists) >= 2:
        for l in lists[1:]:
            ret = [[*x, y] for x in ret for y in l]
    return ret
