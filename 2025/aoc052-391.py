print(sum((lambda l: [(l[i][0] - l[i-1][0]) if l[i-1][1] > 0 else 0 for i in range(1, len(l))] + [0])((lambda l: [l.append((int(x[:-1]), l[-1][1] + (1 if x[-1] == '^' else -1))) or l[-1] for x in sorted([i for j in [[r[0]+'^', str(int(r[1])+1)+'$'] for r in [r.split('-') for r in open('input5').read().split('\n\n')[0].split('\n')]] for i in j], key=lambda a: int(a[:-1]))])([('0^', 0)]))))

'''
file = [r.split('-') for r in open('input5').read().split('\n\n')[0].split('\n')]

offset = [[r[0]+'^', str(int(r[1])+1)+'$'] for r in file]

inlined = [i for j in offset for i in j]

sted = sorted(inlined, key=lambda a: int(a[:-1]))

deeped = (lambda l: [l.append((int(x[:-1]), l[-1][1] + (1 if x[-1] == '^' else -1))) or l[-1] for x in sted])([('0^', 0)])

lengths = (lambda l: [(l[i][0] - l[i-1][0]) if l[i-1][1] > 0 else 0 for i in range(1, len(l))] + [0])(deeped)

total = sum(lengths)

print(total)
'''
