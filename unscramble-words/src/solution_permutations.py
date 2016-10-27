import itertools
from timeit import default_timer as timer

# Start timer
start = timer()

# Read the file
with open("book.txt") as f:
    book = f.read().split()

# Read scrambled words
with open("words.txt") as f:
    words = f.read().split()

# For each word find it's permutations and pick up the ones present in book
result = []
for word in words:
    for permutation in itertools.permutations(word):
        item = ''.join(permutation)
        if item in book:
            result.append(item)
            break

# End timer
end = timer()

# Print result
print 'Soulution: %s' % ','.join(result)
print 'Time taken: %s' % (end-start)
