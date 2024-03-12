def solution(numer1, denom1, numer2, denom2):
    denom = denom2 * denom1
    numer = (denom2 * numer1) + (denom1 * numer2)
    count = 2
    while denom + 1 != count:
        if denom % count == 0 and numer % count == 0:
            denom = denom // count
            numer = numer // count
            count = 2
        else:
            count += 1
    
    return [numer, denom]