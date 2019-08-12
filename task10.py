while True:
    word = input('Input word: ')
    reversed_word = ''.join(reversed(word))
    print(word,reversed_word)

    if word == reversed_word:
        print('It`s polindrom')
    else:
        print('It`s isn`t polindrom')