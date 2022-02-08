#gfdsgfds
#python dictionary
#simplify getting with dictionaries
counts = dict()
names = ['csev','cwen','csev','ziqian','cwen']
for name in names :
    counts[name] = counts.get(name,0) + 1
print(counts)
