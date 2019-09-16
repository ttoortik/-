import math
words = open("words.txt").read().replace('"', '').split(",")
alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0
for word in words:
    letters = 0
    for letter in word:
        letters +=alphabet.index(letter)
        if letters == int(math.sqrt(2*letters)) * (int(math.sqrt(2*letters))+1)/2:
            result+=1
print(result)
