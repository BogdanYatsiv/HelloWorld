sentence = input('Input your sentence: ')
print(sentence)

sentence = sentence.split()

sorted_sentence = sorted(sentence, key = len)
print(sorted_sentence)