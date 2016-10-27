with open("book.txt") as f:
    book = f.read().split()

sortedBook = [''.join(sorted(line)) for line in book]

uniqWords = set()
duplicates = []
for word in sortedBook:
    if word in uniqWords:
        duplicates.append(word)
    else:
        uniqWords.add(word)

if(len(duplicates) > 0):
    print "Duplicates: %s" % duplicates
else:
    print "No duplicates found from book after sorting"
