def popular_words(text, words):

    text = text.lower()

    text_words = text.split()

    word_count = {word: 0 for word in words}

    for word in text_words:
        if word in word_count:
            word_count[word] += 1

    return word_count

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
print('OK')