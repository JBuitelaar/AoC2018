input = open('18_forest.txt').read().splitlines()
from collections import Counter

rows=len(input)
cols=len(input[0])

def evolve(current,row,col,fields):
    nbs=Counter(fields[r][c] for r in range(row-1,row+2) for c in range(col-1,col+2)\
        if 0<=r<rows and 0<=c<cols and not (r==row and c==col))

    if '.' == current:
        return '|' if nbs.get('|',0) >= 3 else '.'
    elif '|' == current:
        return '#' if nbs.get('#',0) >= 3 else '|'
    else:
        assert '#'==current
        return '#' if '#' in nbs and '|' in nbs else '.'

def evolve_all(fields):
    return ["".join(evolve(v,r,c,fields) for c,v in enumerate(row)) for r,row in enumerate(fields)]

def score(input_str:str):
    return input_str.count('#')*input_str.count('|')

def joined(fields):
    return "".join(fields)

print("PART I")
res=input[::]
for _ in range(10):
    res=evolve_all(res)

print(score(joined(res)))

print("PART II")

res=input
seen=[joined(input)]

iterations=1000000000
for j in range(1,iterations+1):
    res=evolve_all(res)
    key=joined(res)

    try:
        ix=seen.index(key)
        freq=j-ix
        n=(iterations-ix)%freq
        print(ix,j,n)
        print(score(seen[ix+n]))
        break
    except ValueError:
        seen.append(key)



