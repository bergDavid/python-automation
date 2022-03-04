#Objects python
#Create a Class (template):
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
# same sintexe
# PartyAnimal.party(an)
an.party()
an.party()