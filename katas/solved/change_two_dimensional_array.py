# Solved!

def matrix(array):
    res = []
    subs = [x for x in array]
    i = 0
    for y in subs:
        lst = []
        j = 0
        for z in y:
            if j == i:
                if z >= 0: lst.append(1)
                else: lst.append(0)
            else: lst.append(z)
            j += 1
        i += 1
        res.append(lst)
    return res


if __name__ == "__main__":
    assert matrix([[27, 62, 27, -93], [-33, -56, 43, 71], [66, 30, 36, 91], [49, 77, -36, -44]]) == [[1, 62, 27, -93], [-33, 0, 43, 71], [66, 30, 1, 91], [49, 77, -36, 0]] 