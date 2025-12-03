print(sum(int(''.join((lambda l: [l.append((lambda p, j: p[:-1] + (lambda l: [[l.append([i, x]) or l[-1] for i, x in enumerate(p[-1][:-j] if j > 0 else p[-1]) if int(x) > int(l[-1][1])][-1][1]] + [p[-1][l[-1][0]+1:]])([[-1, 0]]))(l[-1], j)) or l[-1] for j in range(11, -1, -1)][-1])([[bank]])[:12])) for bank in open('input3').read().rstrip().split()))

'''
file = open('input3').read().rstrip().split()

#rerunner = (lambda l: [l.append(f"f({i},{l[-1]})") or l[-1] for i in range(12)][-1])(['0', bank])

acc = 0
for bank in file:
    sum_lambda = lambda p, j: p[:-1] + (lambda l: [[l.append([i, x]) or l[-1] for i, x in enumerate(p[-1][:-j] if j > 0 else p[-1]) if int(x) > int(l[-1][1])][-1][1]] + [p[-1][l[-1][0]+1:]])([[-1, 0]])

    sums = (lambda l: [l.append(sum_lambda(l[-1], j)) or l[-1] for j in range(11, -1, -1)][-1])([[bank]])

    res = int(''.join(sums[:12]))

    acc += res

    print(bank)
    print(sums)
    print(res)

print(acc)
'''
