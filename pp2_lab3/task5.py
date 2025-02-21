import itertools

def p():
    a = input()
    permutations = itertools.permutations(a)
    for i in permutations:
        print(''.join(i))

p()
