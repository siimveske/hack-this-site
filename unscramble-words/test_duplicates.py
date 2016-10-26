f = open("wordlist.txt")
d = f.read()
f.close()

result = []
for i in d.split():
    result.append(''.join(sorted(i)))

seen = set()
uniq = []
for x in result:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
    else:
        print x
