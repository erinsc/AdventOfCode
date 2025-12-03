print(sum(int((lambda s: s[0] + (lambda l: [l.append(x) or l[-1] for x in s[1] if int(x) > int(l[-1])][-1])([0]))((lambda l: [[l.append([i, x]) or l[-1] for i, x in enumerate(bank[:-1]) if int(x) > int(l[-1][1])][-1][1]] + [bank[l[-1][0]+1:]])([[-1, 0]]))) for bank in open('input3').read().rstrip().split()))

'''
file = open('input3').read().rstrip().split()

acc = 0
for bank in file:
    sums = (lambda l: [[l.append([i, x]) or l[-1] for i, x in enumerate(bank[:-1]) if int(x) > int(l[-1][1])][-1][1]] + [bank[l[-1][0]+1:]])([[-1, 0]])
    sums2 = (lambda s: s[0] + (lambda l: [l.append(x) or l[-1] for x in s[1] if int(x) > int(l[-1])][-1])([0]))(sums)

    acc += int(sums2)

    print(bank)
    print(sums)
    print(sums2)

print(acc)
'''
