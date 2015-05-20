def rotate(word):
    return word[-1:] + word[:-1]

list = []
frenchers = []
dict = open('/usr/share/dict/words', 'r')

for word in dict:
    if "'" not in word:
        list.append(word.strip().lower())

print str(len(list)) + " words"

for word in list:
    original_word = word
    for i in range(0, len(word)):
        word = rotate(word)
        if word not in list:
            break
        else:
            if i == len(word) - 1:
                frenchers.append(original_word)

print str(len(frenchers)) + " frenchers found."
for frencher in frenchers:
    print frencher
