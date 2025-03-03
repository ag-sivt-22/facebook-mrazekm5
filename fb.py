from collections import deque


class Facebook():
    def __init__(self):
        self.list = {}
    def pridej_uzivatel(self,jmeno):
        self.list[jmeno] = (Uzivatel(jmeno))
    def pridej_znamost(self,clovek1,clovek2):
        self.list[clovek1].pridej_znamost(self.list[clovek2])
        self.list[clovek2].pridej_znamost(self.list[clovek1])

class Uzivatel():
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.zn = []
    def pridej_znamost(self,clovek2):
        self.zn.append(clovek2)
    def jak_daleko(self,clovek2):
        self.list=[]       
        self.deck=deque()
        for zn in self.zn:
            self.deck.append((zn,0))
            self.list.append(zn)
        while(self.deck):
            self.x = self.deck.popleft()
            if (self.x[0]==clovek2): return self.x[0],self.x[1]
            for n in self.x[0].zn:
                if (n not in self.list):
                    self.deck.append((n,self.x[1]+1))
                    self.list.append(n)
                    if (n==clovek2):
                        return n,self.x[1]+1
        return None


# Vytvoření instance Facebooku
fb = Facebook()

# Seznam unikátních jmen
jmena = [
    "Adam", "Beata", "Cyril", "Dana", "Emil", "František", "Gabriela", "Hana", "Ivan", "Jana",
    "Karel", "Lenka", "Marek", "Nina", "Ondřej", "Petra", "Quentin", "Radka", "Stanislav", "Tereza",
    "Urbán", "Veronika", "Walter", "Xenie", "Yvona", "Zdeněk", "Alex", "Blanka", "Cecilie", "David"
]

# Vkládání známostí do Facebooku
for jmeno in jmena:
    fb.pridej_uzivatel(jmeno)
  
# Hardkodované známosti
znamosti = [
    ("Adam", "Beata"), ("Adam", "Cyril"), ("Beata", "Dana"),
    ("Cyril", "Emil"), ("Cyril", "František"), ("Dana", "Gabriela"),
    ("Emil", "Hana"), ("František", "Ivan"), ("Gabriela", "Jana"),
    ("Hana", "Karel"), ("Ivan", "Lenka"), ("Jana", "Marek"),
    ("Karel", "Nina"), ("Lenka", "Ondřej"), ("Marek", "Petra"),
    ("Nina", "Quentin"), ("Ondřej", "Radka"), ("Petra", "Stanislav"),
    ("Quentin", "Tereza"), ("Radka", "Urbán"), ("Stanislav", "Veronika"),
    ("Tereza", "Walter"), ("Urbán", "Xenie"), ("Veronika", "Yvona"),
    ("Walter", "Zdeněk"), ("Xenie", "Alex"), ("Yvona", "Blanka"),
    ("Zdeněk", "Cecilie"), ("Alex", "David"), ("Blanka", "Adam")
]

# Vkládání známostí do Facebooku
for clovek1, clovek2 in znamosti:
    fb.pridej_znamost(clovek1, clovek2)

z=fb.list["Adam"].jak_daleko(fb.list["Beata"])
print(z[0].jmeno,z[1],z)

x=fb.list["Adam"].jak_daleko(fb.list["Urbán"])
print(x[0].jmeno,x[1],x)




