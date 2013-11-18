from time import *
from random import *
from ??? import*

def lahing(monster,tegevus):
    sa=SA()
    sd=SD()
    if SCA()==True:
        sa+=1
    ka=monster.KA()
    kd=monster.KD()
    if monster.KCA()==True:
        ka+=1
    ktegevus=monster.KTEGEVUS()
    if tegevus=="d":
        sd*=3
    if tegevus=="a":
        sa*=2
    if ktegevus==0:
        kd*=3
    if ktegevus==1:
        ka*=2
    if scrit()==True:
        sa*=2
    if kcrit()==True:
        ka*=2
    if tegevus=="h":
        Heal()
    sleep(1)
    tulem=0
    for i in range(sa):
        jõud=randrange(getrangesa())
        tulem+=jõud
    for i in range(kd):
        jõud=randrange(monster.getrangekd())
        tulem-=jõud
    if tulem>0:
        monster.Kelud(tulem)
    else:
        monster.KCAK(True)
        
    tulem=0
    sleep(1)
    for i in range(ka):
        jõud=randrange(monster.getrangekd())
        tulem+=jõud
    for i in range(sd):
        jõud=randrange(getrangesd())
        tulem-=jõud
    if tulem>0:
        Elud(tulem)
    else:
        SCAK(True)
        
    
    
