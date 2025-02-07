import itertools

def string_permutations():
    user_input = input()
    permutations = itertools.permutations(user_input)
    for perm in permutations:
        print(''.join(perm))

string_permutations()
