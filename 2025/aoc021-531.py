print(sum([i for r in [[[int(str(x)+str(x)) for x in range(r[0], r[1]+1)], r[2], r[3]] for r in [[int(r[0][:len(r[0])//2]), int(r[1][:len(r[1])//2]), int(r[0]), int(r[1])] for r in [r for r in [i for j in [[[r[0], '9' * len(r[0])]] + [['1'+'0'*x, '9'*(x+1)] for x in range(len(r[0]), len(r[1])-1)] + [['1' + '0'*(len(r[1])-1), r[1]]] if len(r[0]) < len(r[1]) else [r] for r in [s.split('-') for s in open('input2').read().rstrip().split(',')]] for i in j] if len(r[0]) % 2 == 0]]] for i in [x for x in r[0] if r[1] <= x <= r[2]]]))

'''
file = open('input2').read().rstrip().split(',')
ranges = [s.split('-') for s in file]
equalized = [[[r[0], '9' * len(r[0])]] + [['1'+'0'*x, '9'*(x+1)] for x in range(len(r[0]), len(r[1])-1)] + [['1' + '0'*(len(r[1])-1), r[1]]] if len(r[0]) < len(r[1]) else [r] for r in ranges]
inlined = [i for j in equalized for i in j]
filtered = [r for r in inlined if len(r[0]) % 2 == 0]

split = [[int(r[0][:len(r[0])//2]), int(r[1][:len(r[1])//2]), int(r[0]), int(r[1])] for r in filtered]
ranged = [[[int(str(x)+str(x)) for x in range(r[0], r[1]+1)], r[2], r[3]] for r in split]
retained = [i for r in ranged for i in [x for x in r[0] if r[1] <= x <= r[2]]]

print(sum(retained))
'''
