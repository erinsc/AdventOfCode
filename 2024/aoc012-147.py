print(sum(sum(int(a) * sum(b == a for b in sorted(B)) for a in sorted(A)) for A, B in [zip(*[l.split() for l in open('input1.txt').readlines()])]))
