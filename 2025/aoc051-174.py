print((lambda f: sum(any(r[0] <= int(n) <= r[1] for r in [[int(y) for y in x.split('-')] for x in f[0].split()]) for n in f[1].split()))(open('input5').read().split('\n\n')))

'''
file = open('input5').read().split('\n\n')

ranges = [[int(y) for y in x.split('-')] for x in file[0].split()]

numbers = [int(y) for y in file[1].split()]

total = sum(any(r[0] <= n <= r[1] for r in ranges) for n in numbers)


print(total)
'''
