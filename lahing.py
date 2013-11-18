from random import *
from database import *

def lahing(tegevus,char):                #monster=number
    mon=char.uuskoletis(monster)
    if tegevus=='h':
        char.Heal()
    elif tegevus=='a':
        ca=randint(char.W.mindam,char.W.maxdam)+char.boonus
        char.boonus=0
        if randint(0,100/wep.crit)==0:      #crit
            ca*=2
        if randint(0,1)==0:                 #koletis ründab
            ma=randint(0,mon.attack)
            if ca>ma:
                mon.hp-=ca-ma
            elif ma>ca:
                char.hp-=ma-ca
            else:
                print('You both attack with equal force!')
        else:                               #koletis kaitseb
            ma=randint(0,mon.defence)
            if ca>ma:
                mon.hp-=ca-ma
            else:
                print('Monster defended successfully!')
    elif tegevus=='d':
        char.boonus+=arm.defence
        if randint(0,1)==1:                 #koletis kaitseb
            print('None of you are brave enough to attack.')
        else:                               #koletis ründab
            ca=randint(0,arm.defence)
            ma=randint(0,mon.attack)
            if ma>ca:
                char.hp-=ma-ca
            else:
                print('You defended successfully!')
    if mon.hp<=0:
        print("The",mon.name,"is DEAD!")    #lahing over
    if char.hp<=0:
        print("You are DEAD!")              #GAME OVER
        
    print("koletise elud",mon.hp)           #lahingu kontroll...
    print("sinu elud",char.hp)              #lahingu kontroll...
