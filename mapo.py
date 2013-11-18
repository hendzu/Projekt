def loo_kaart(kaart):
    Kaart="maps/"+kaart
    fail=open(Kaart)
    global rows
    global columns
    columns=int(fail.readline())
    rows=int(fail.readline())
    global MAP
    MAP=[]
    ROW=[]
    for i in range(rows):
        ROW=list(fail.readline().strip())
        MAP.append(ROW)
    global Kangelane
    Kangelane=find("K",True)
def find(K,T=False):
    x=0
    y=0
    while x<rows:
        y=0
        while y<columns:
            if K in MAP[x][y]:
                Tegelane=[x,y]
                if T==True:
                    MAP[x][y]=".K"
                    y+=columns
                    x+=rows
            y+=1
        x+=1
    return Tegelane
def out():
    Row=[]
    Column=[]
    for i in range(11):
        Row=[]
        for ii in range(11):
            Row.append(MAP[Kangelane[0]-5+i][Kangelane[1]-5+ii])
        Column.append(Row)
    return Column
def LEFT():
    if MAP[Kangelane[0]][Kangelane[1]-1]==".":
        MAP[Kangelane[0]][Kangelane[1]]=MAP[Kangelane[0]][Kangelane[1]].strip("K")
        MAP[Kangelane[0]][Kangelane[1]-1]+="K"
        Kangelane[1]-=1
def RIGHT():
    if MAP[Kangelane[0]][Kangelane[1]+1]==".":
        MAP[Kangelane[0]][Kangelane[1]]=MAP[Kangelane[0]][Kangelane[1]].strip("K")
        MAP[Kangelane[0]][Kangelane[1]+1]+="K"
        Kangelane[1]+=1
def UP():
    if MAP[Kangelane[0]-1][Kangelane[1]]==".":
        MAP[Kangelane[0]][Kangelane[1]]=MAP[Kangelane[0]][Kangelane[1]].strip("K")
        MAP[Kangelane[0]-1][Kangelane[1]]+="K"
        Kangelane[0]-=1
def DOWN():
    if MAP[Kangelane[0]+1][Kangelane[1]]==".":
        MAP[Kangelane[0]][Kangelane[1]]=MAP[Kangelane[0]][Kangelane[1]].strip("K")
        MAP[Kangelane[0]+1][Kangelane[1]]+="K"
        Kangelane[0]+=1
