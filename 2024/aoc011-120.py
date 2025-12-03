print(sum(abs(int(a) - int(b)) for a,b in zip(*map(sorted, zip(*[l.split() for l in open('input1.txt').readlines()])))))
