"""
Code Fragment 10.1
Application: Coutning Word Frequencies
A program for counting word frequencies ina  document, and
reporting the most frequent word.

Converts input to lowercase and ignore any nonalphabetic
characters
"""

freq = {}

filename = input("Enter filename")
for piece in open(filename).read().split():
    # print(piece)
    word = ''.join(c for c in piece if c.isalpha()).lower()
    # print(word)
    if word:
        freq[word] = freq.get(word, 0) + 1

# most_frequent = 0
max = 0
for k, v in freq.items():
    if v > max:
        # print("Max: {} and v: {}".format(max,v))
        most_frequent = k
        max = v
        # print(max)

print(freq)
print("The most frequent word is: ", most_frequent)
print("The number of occurrences is: ", max)