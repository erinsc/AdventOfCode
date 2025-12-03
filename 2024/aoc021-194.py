print(sum([all(abs(v)<=3 for v in d)*(all(v<0 for v in d)+all(v>0 for v in d))for d in[[a-b for a,b in zip(l,l[1:])]for l in [list(map(int,l.split()))for l in open('input2.txt').readlines()]]]))

