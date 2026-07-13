def longest_word_in_sentence(sentence):
    words = sentence.split()
    longest = ""
    for word  in words:
        if len(word) > len(longest):
            longest = word
    return longest

sentence = input("Enter a sentence: ")
print(longest_word_in_sentence(sentence))