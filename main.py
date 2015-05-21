# Function that moves the last character to the front of a word.
def rotate(word):
    return word[-1:] + word[:-1]

# Create a collection for the list of words and frenchers
list = []
frenchers = []

# Three dictionary options
# dict = open('/usr/share/dict/words', 'r')
dict = open('long.txt', 'r')
# dict = open('short.txt', 'r')

# Iterate through all words in the dictionary to find
# candidates, disqualifying all words fewer than three
# characters in length.
for word in dict:
    if len(word.strip()) > 2:
        list.append(word.strip().lower())

# Print length of candidate word list
print str(len(list)) + " words in dictionary three letters or longer."

# Iterate through each word in candidate word list
for word in list:
    original_word = word

    # Rotate once for each letter in the candidate word
    for i in range(0, len(word)):
        word = rotate(word)
        if word not in list:

            # If one rotation does not appear in the word list,
            # stop inspecting rotations of that word.
            break
        else:
            if i == len(word) - 1:

                # If the rotated word is in the list and we've
                # exhausted all the rotations for that word,
                # add the original word to the list of frenchers.
                print "found: " + original_word
                frenchers.append(original_word)

print str(len(frenchers)) + " frenchers found."
