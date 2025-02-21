def reverse_words():
    a = input()
    words = a.split() 
    reversed_sentence = ' '.join(reversed(words)) 
    return reversed_sentence

print(reverse_words())
