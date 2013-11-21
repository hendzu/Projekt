#character sheet
'''char creationis:
char=char('nimi')
wep=char.uusrelv(0)
arm=char.uusarmor(0)
monster=char.uuskoletis(0)
pot=0
'''

class char:
    def __init__(self, name,gender):
        self.name=name
        self.hp=100
        self.gender=gender
        self.pot=0
        self.W=weapons[0]
        self.A=armors[0]
        self.M=None
        self.boonus=0
    def uusrelv(self, W):
        self.W=weapons[W]
    def uusarmor(self, A):
        self.A=armors[A]
    def uuskoletis(self, M):
        self.M=monsters[M]
    def uuspot(self):
        self.pot+=1
    def Heal(self):
        if self.pot>0:
            self.hp+=50
            self.pot-=1
            print("You healed yourself.")
        elif self.pot<1:
            print("You don't have any potions!")
            
#koletis

class monster:
    def __init__(self,name,attack,defence,pic):
        self.name=name
        self.hp=100
        self.attack=attack
        self.defence=defence
        self.pic=pic
monsters=[monster(' ',0,0," "),
          monster('Teddy',10,5,"T"), #1. mob (drop +1 pot)
          monster('Mummy',15,10,"M"), #2. mob (drop +2 pot)
          monster('Mihkel-Hunter',30,10,"H"),
          monster('Something Bad Guy',60,40,"B")] #3. mob
        
#relvad

class weapon:
    def __init__(self,name,mindam,maxdam,crit,pic):
        self.name=name
        self.mindam=mindam
        self.maxdam=maxdam
        self.crit=crit/100
        self.pic=pic
weapons=[weapon(' ',0,12,1," "),
         weapon('Branch',2,10,5,"b"), #1. mobi drop
         weapon('Sword',10,20,10,"s")] #2. mobi drop


class armor:
    def __init__(self,name,defence,pic):
        self.name=name
        self.defence=defence
        self.pic=pic
armors=[armor(' ',0," "),
        armor('Cloak',5,"c"), #1. mobi drop
        armor('Chainmail',20,"m")] #2. mobi drop



