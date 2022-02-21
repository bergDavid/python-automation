#Exercise
counts = dict()
line = "the general text general text text"
words = line.split()
print("words", words)
print("counting...")
for word in words:
    counts[word] = counts.get(word,0) + 1
#print("Counts",counts)
#for key in counts:
#    print(key,counts[key])
print(counts.items())