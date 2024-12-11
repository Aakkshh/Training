def find_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

sentence = "The quick brown fox jumps over the lazy dog"
print(find_word(sentence))