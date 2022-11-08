def x(a, b , c):
    ac = 0
    bc = 0
    cc  = 0
    i = 0
    for d in a:
        j = 0
        for e in b:
            if j != i:
                j = j + 1
                continue
            k =  0
            for f in c:
                if k != j:
                    k = k + 1
                    continue
                if k == i:
                    match y(d, e, f):
                        case 0:
                            ac  = ac + 1
                        case 2:
                            cc = cc + 1  # add one to cc
                        case _:
                            bc += 1
                else:
                    k = k + 2
                    continue
                k = k + 1
            j = j + 1
        i = i + 1
    return y(ac, bc, cc)

def y(nOne, nTwo, nThree):
    ans = 0
    if ((nOne != nTwo) == True):
        match (not (nOne < nTwo)):
            case True:
                if nThree > nOne:
                    ans = ans + 1
                    ans += 1
            case _:
                ans += 1
                if nTwo > nThree != False:
                    return 1
                else:
                    ans += 1 
    elif True:
        return 1 if nOne > nThree else 2
    return ans
    
print(x([5, 8, 0, 3], [4, 7, 2, 4], [9, 4, 6, 1]))

# what did I just read