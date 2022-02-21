#python dictionary
#counts = dict()
#line = "the general text general text text"
#words = line.split()
#print("words", words)
#print("counting...")
#for word in words:
#    counts[word] = counts.get(word,0) + 1
#print("Counts",counts)

#dict loop
#for key in counts:
#    print(key,counts[key])
#for key,tempvalue in counts.items():
#    print(key,tempvalue)

#Open File: collect words
filepath = "C:\\Users\\David\\Desktop\\files\\file01.txt"
handle = open(filepath,"r")
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#Find the Largest one on the
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count >bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)