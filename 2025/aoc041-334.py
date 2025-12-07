print((lambda b: sum((lambda x, y: (len((b[y-1][x-1:x+2] + b[y][x-1] + b[y][x+1] + b[y+1][x-1:x+2]).replace('.','')) < 4) * (b[y][x] == '@'))(x,y) for x in range(1,len(b[0])-1) for y in range(1,len(b)-1)))((lambda l: ['.' * (len(l[0])+2)] + ['.' + x + '.' for x in l] + ['.' * (len(l[0])+2)])(open("input4a").read().rstrip().split())))

'''
file = open("input4").read().rstrip().split()

buffered = (lambda l: ['.' * (len(l[0])+2)] + ['.' + x + '.' for x in l] + ['.' * (len(l[0])+2)])(file)

b = buffered

z = lambda x, y: (len((b[y-1][x-1:x+2] + b[y][x-1] + b[y][x+1] + b[y+1][x-1:x+2]).replace('.','')) < 4) * (b[y][x] == '@')

acc = 0
for x in range(1,len(b[0])-1):
    for y in range(1,len(b)-1):
        acc += z(x,y)

print(acc)
'''
