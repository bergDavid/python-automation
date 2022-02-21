#python tuples
# tuples are imutable
# c = {'a':10,'b':1,'c':22}
# temp = list()
# for k,v in c.items():
#     temp.append((v,k))
# print(temp)
# tmp = sorted(temp,reverse=True)
# print(tmp)


# #Open File: collect words
# filepath = "C:\\Users\\David\\Desktop\\files\\file01.txt"
# handle = open(filepath,"r")
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1

# #Find the Largest one on the
# lst = list()
# for key,val in counts.items():
#     newtup = (val,key)
#     lst.append(newtup)
# lst = sorted(lst,reverse = True)
# for val,key in lst[:5]:
#     print(key,val)

c = {'a':10,'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()]))
