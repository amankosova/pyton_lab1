def reverse_words():
    user_input = input()
    words = user_input.split() 
    reversed_sentence = ' '.join(reversed(words)) 
    return reversed_sentence

print(reverse_words())
