print(sum(eval(op.join(x)) for *x, op in zip(*[r.split() for r in open("input6").read().rstrip().split('\n')])))

'''
file = [r.split() for r in open("input6").read().rstrip().split('\n')]

doned = [eval(op.join(x)) for *x, op in zip(*file)]

print(sum(doned))
'''
