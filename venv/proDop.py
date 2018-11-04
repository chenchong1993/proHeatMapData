import json

def readfile():
    f = open("E:\python-workspace\proHeatMapData\\200HObs", 'r')
    str = f.read()
    return str
filestr = readfile()
filelist = filestr.split("*")[1:]
HDOPdic = {}
VDOPdic = {}
PDOPdic = {}
GDOPdic = {}
Rssdic = {}
i = 1
for item in filelist:
    itemlist = item.split(',')
    # print(itemlist)
    B = float(itemlist[0])
    L = float(itemlist[1])
    HDOP = float(itemlist[4])
    VDOP = float(itemlist[5])
    PDOP = float(itemlist[6])
    GDOP = float(itemlist[7])
    Rss = float(itemlist[8][:-1])
    if  ((38.24762<B)and(B<38.24783) and(114.34855<L)and(L<114.34933)):
        HDOPdic[str(i)] = [B,L,HDOP]
        VDOPdic[str(i)] = [B,L, VDOP]
        PDOPdic[str(i)] = [B,L, PDOP]
        GDOPdic[str(i)] = [B,L, GDOP]
        Rssdic[str(i)] = [B,L ,Rss]
    else:
        pass
    i = i + 1
    # print(HDOP,VDOP,PDOP,GDOP,Rss)
HDOPjs= json.dumps(HDOPdic)
VDOPjs= json.dumps(VDOPdic)
PDOPjs= json.dumps(PDOPdic)
GDOPjs= json.dumps(GDOPdic)
Rssjs= json.dumps(Rssdic)
print(HDOPjs)
print(VDOPjs)
print(PDOPjs)
print(GDOPjs)
print(Rssjs)
# print(filelist[0])