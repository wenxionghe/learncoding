# This is my first program. Basically it removes the first letter of the word and add "ay" at the end of it.
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    answer = word[1:len(original)]
    new_word = answer + first + pyg
    print new_word
else:
    print 'You didn''t type in any word son!'
