f = open("wordlist.txt")
book = f.read().split()
f.close()

words = '''
yaldgbu
ktbaasbe
eetysw
xilsae
menacr
gesanl
nraibas
igcmab
ikatin
milana
'''

result = []
sortedWords = [''.join(sorted(line)) for line in words.split()]
sortedBook = [''.join(sorted(line)) for line in book]
for word in sortedWords:
    result.append(book[sortedBook.index(word)])

print ','.join(result)


