#python regex
# ^ match the start of the line
#. match any character
# * meny times
import re
filepath = "C:\\Users\\David\\Desktop\\files\\file01.txt"
handle = open(filepath,"r")
for line in handle:
    words = line.split()
    for word in words:
        if re.search("Real",word):
            print(word)
