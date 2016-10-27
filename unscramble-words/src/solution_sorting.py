from timeit import default_timer as timer

# Start timer
start = timer()

# Read the file
with open("book.txt") as f:
    book = f.read().split()

# Read scrambled words
with open("words.txt") as f:
    words = f.read().split()

# Sort words in book and words list.
# Compare sorted items and use matched index to
# to fetch the right word from book
result = []
sortedWords = [''.join(sorted(line)) for line in words]
sortedBook = [''.join(sorted(line)) for line in book]
for word in sortedWords:
    result.append(book[sortedBook.index(word)])

# End timer
end = timer()

# Print result
print 'Soulution: %s' % ','.join(result)
print 'Time taken: %s' % (end-start)
