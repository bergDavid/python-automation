#Objects python
#Create a Class (template):
# dir() list the commands on a object

# class PartyAnimal:
#     x = 0
#     def party(self):
#         self.x = self.x + 2
#         print(self.x)

# an = PartyAnimal()
# # same sintexe
# # PartyAnimal.party(an)
# an.party()
# an.party()

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)
    #def __del__(self):
    #    print(self.name + "deleted")

#q = PartyAnimal('Quincy')
# m = PartyAnimal('Miya')
# q.party()
# m.party()
# q.party()

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name," points ", self.points)

s = PartyAnimal("Sally")
s.party()
j = FootballFan("Jim")
j.party()
j.touchdown()
