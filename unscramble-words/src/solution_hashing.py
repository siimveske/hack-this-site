from timeit import default_timer as timer

# Start timer
start = timer()

with open("book.txt") as f:
    book = f.read().split()

with open("words.txt") as f:
    words = f.read().split()

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
# http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

# Variable to map Char => PrimeNumber
alphabet = {}
generator = gen_primes()

# Get characters present in book and
# map each charater to a prime number
for letter in ''.join(book):
    if letter not in alphabet:
        alphabet[letter] = generator.next()

# Use map to transform each line in words.txt into a unique prime number
needle_list = []
for word in words:
    needle = 1
    for character in word:
        needle *= alphabet[character]
    needle_list.append(needle)

# Use map to transform each line in boook.txt into a unique prime number
haystack = []
for word in book:
    wHash = 1
    for character in word:
        wHash *= alphabet[character]
    haystack.append(wHash)

# Find calculated word and use it's index to get correct word from book
result = []
for needle in needle_list:
    result.append(book[haystack.index(needle)])

# End timer
end = timer()

# Print result
print 'Soulution: %s' % ','.join(result)
print 'Time taken: %s' % (end-start)
