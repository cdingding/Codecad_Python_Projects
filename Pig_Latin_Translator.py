# Pig Latin Project

pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'
word=original.lower()
first=word[0]
new_word=word[1:len(word)]
new_word=new_word+first+pyg
print new_word