print(sum(1 for s in (lambda r: [r.append(r[-1] + x) or r[-1] for x in [x for y in list(map(lambda n: [n // abs(n)] * abs(n), list(map(lambda s: int(s[1:]) * (1 if s[0] == 'R' else -1), open("input1").read().split())))) for x in y]])([50]) if s % 100 == 0))

'''
file = open("input1").read().split()

nums = list(map(lambda s: int(s[1:]) * (1 if s[0] == 'R' else -1), file))

nums2 = list(map(lambda n: [n // abs(n)] * abs(n), nums))

nums3 = [x for y in nums2 for x in y]

sums = (lambda r: [r.append(r[-1] + x) or r[-1] for x in nums3])([50])

total = sum(1 for s in sums if s % 100 == 0)

print(total)
'''
