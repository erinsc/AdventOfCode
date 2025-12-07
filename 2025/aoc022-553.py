print(sum(sum(int(c) for c in set(str(x)*(len(test[-1]) // d) for d in test[:-2] for x in range(int(test[-2][:d]), int(test[-1][:d])+1) if test[-2] <= str(x)*(len(test[-1]) // d) <= test[-1])) for test in [[x for x in range(1, len(r[0])) if len(r[0]) % x == 0] + r for r in [r for j in [[[r[0], '9' * len(r[0])]] + [['1'+'0'*x, '9'*(x+1)] for x in range(len(r[0]), len(r[1])-1)] + [['1' + '0'*(len(r[1])-1), r[1]]] if len(r[0]) < len(r[1]) else [r] for r in [s.split('-') for s in open('input2').read().rstrip().split(',')]] for r in j if len(r) > 1]]))

'''
file = open('input2').read().rstrip().split(',')
ranges = [s.split('-') for s in file]
equalized = [[[r[0], '9' * len(r[0])]] + [['1'+'0'*x, '9'*(x+1)] for x in range(len(r[0]), len(r[1])-1)] + [['1' + '0'*(len(r[1])-1), r[1]]] if len(r[0]) < len(r[1]) else [r] for r in ranges]
filtered = [r for j in equalized for r in j if len(r) > 1]

viable = [[x for x in range(1, len(r[0])) if len(r[0]) % x == 0] + r for r in filtered]

print(viable)

acc = 0
for test in viable:
    corrects = set(str(x)*(len(test[-1]) // d) for d in test[:-2] for x in range(int(test[-2][:d]), int(test[-1][:d])+1) if test[-2] <= str(x)*(len(test[-1]) // d) <= test[-1])

    print(corrects)

    acc += sum(int(c) for c in corrects)

print(acc)
'''
