from itertools import permutations
print([int(''.join(i)) for i in permutations('0123456789')][999999])
