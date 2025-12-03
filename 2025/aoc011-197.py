print(sum(1 for s in (lambda nums: [(50 + sum(nums[:e])) % 100 for e in range(len(nums)+1)])(list(map(lambda s: int(s[1:]) * (1 if s[0] == 'R' else -1), open("input1").read().split()))) if s == 0))

'''
file = open("input1").read().split()

nums = list(map(lambda s: int(s[1:]) * (1 if s[0] == 'R' else -1), file))

sums = (lambda nums: [(50 + sum(nums[:e])) % 100 for e in range(len(nums)+1)])(nums)

total = sum(1 for s in sums if s == 0)

print(total)
'''
