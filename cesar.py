import sys

if len(sys.argv) <2:
    sys.exit("missing phrase to decode")
phrase = sys.argv[1].lower()

letters = ['a','b', 'c', 'd','e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n','o','p','q', 'r','s', 't','u', 'v', 'w','x', 'y', 'z']
num_letters = len(letters)

def getnewletter(character, shift):
    """Calculates new letter applying the specified shifting value. """
    if character in letters:
        newi = letters.index(character) + shift
        if newi + i >= num_letters:
            newi = newi-num_letters

        return letters[newi]
    else:
        return character

# now print all the options
for i in range(1, num_letters):
    newphrase=""
    for c in phrase:
        newletter = getnewletter(c,i)
        newphrase = newphrase + newletter
    print(i, newphrase)
