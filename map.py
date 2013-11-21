from tkinter import *
from pics import *
def loo_kaart(kaart):
    Kaart="maps/"+kaart
    file=open(Kaart)
    global MAP
    MAP=[]
    for line in file:
        Line=line.strip()
        ROW=list(Line)
        MAP.append(ROW)
    global Kangelane
    Kangelane=find("K")
    Joonista()

def delfrommap(x,y):
    MAP[Kangelane[0]+x][Kangelane[1]+y]="."
    Map[Kangelane[0]+x][Kangelane[1]+y]=PhotoImage(file=get_pic("."))

def Joonista():
    global Map
    Map=[]
    for x in MAP:
        Row=[]
        for y in x:
            Row.append(PhotoImage(file=get_pic(y)))
        Map.append(Row)
def find(K):
    x=0
    while x<len(MAP):
        y=0
        while y<len(MAP[0]):
            if K in MAP[x][y]:
                Tegelane=[x,y]
                MAP[x][y]="."
                x+=len(MAP)
                y+=len(MAP[0])
            y+=1
        x+=1
    return Tegelane
def out():
    return Kangelane,Map
def LEFT():
    if MAP[Kangelane[0]][Kangelane[1]-1]==".":
        Kangelane[1]-=1
    else:
        return MAP[Kangelane[0]][Kangelane[1]-1]
def RIGHT():
    if MAP[Kangelane[0]][Kangelane[1]+1]==".":
        Kangelane[1]+=1
    else:
        return MAP[Kangelane[0]][Kangelane[1]+1]
def UP():
    if MAP[Kangelane[0]-1][Kangelane[1]]==".":
        Kangelane[0]-=1
    else:
        return MAP[Kangelane[0]-1][Kangelane[1]]
def DOWN():
    if MAP[Kangelane[0]+1][Kangelane[1]]==".":
        Kangelane[0]+=1
    else:
        return MAP[Kangelane[0]+1][Kangelane[1]]
