import json
import pymysql.cursors




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
HDOPdic3 = {}
VDOPdic3 = {}
PDOPdic3 = {}
GDOPdic3 = {}
Rssdic3 = {}
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
    if  ((38.24762<B)and(B<38.24783) and(114.34855<L)and(L<114.34938)):
        HDOPdic[str(i)] = [B,L,HDOP]
        VDOPdic[str(i)] = [B,L, VDOP]
        PDOPdic[str(i)] = [B,L, PDOP]
        GDOPdic[str(i)] = [B,L, GDOP]
        Rssdic[str(i)] = [B,L ,Rss]
        if ((38.24762<B)and(B<38.24783) and(114.34855<L)and(L<114.34873)):
            HDOPdic3[str(i)] = [B, L, HDOP]
            VDOPdic3[str(i)] = [B, L, VDOP]
            PDOPdic3[str(i)] = [B, L, PDOP]
            GDOPdic3[str(i)] = [B, L, GDOP]
            Rssdic3[str(i)] = [B, L, Rss]
    else:
        pass
    i = i + 1
    # print(HDOP,VDOP,PDOP,GDOP,Rss)
HDOPjs= json.dumps(HDOPdic)
VDOPjs= json.dumps(VDOPdic)
PDOPjs= json.dumps(PDOPdic)
GDOPjs= json.dumps(GDOPdic)
Rssjs= json.dumps(Rssdic)
HDOPjs3= json.dumps(HDOPdic3)
VDOPjs3= json.dumps(VDOPdic3)
PDOPjs3= json.dumps(PDOPdic3)
GDOPjs3= json.dumps(GDOPdic3)
Rssjs3= json.dumps(Rssdic3)

print(HDOPjs)
print(HDOPjs3)
print(VDOPjs)
print(PDOPjs)
print(GDOPjs)
print(Rssjs)
# print(filelist[0])

def get_conn():
    """======连接数据库========="""
    conn = pymysql.connect(
        host='121.28.103.199',
        port=5571,
        user='root',
        passwd='casmadmin2018',
        db='platformdata',
        charset='utf8',
        #"""===关闭自动提交""",
        autocommit = False
    )
    return conn

def update(DOPjs,typed,floord):
    """
    改变
    :return:
    """
    conn = get_conn()
    print(conn)
    try:
        """===联系上下文使用with语句赋给cursor"""
        with conn.cursor() as cursor:
            """===写出sql语句==="""
            sql = "update heatmapdata set data= "+ "'" + DOPjs + "'" +  "where type =  "+ "'" + typed + "'" +  "and floor="+ "'" + floord + "'" +  " "
            """===执行sql语句==="""
            cursor.execute(sql)
            """===提交事务==="""
            conn.commit()
            print(cursor.rowcount)
    except Exception as e:
        print('出现问题' + str(e))
        """===事务回滚==="""
        conn.rollback()
    finally:
        """===关闭连接==="""
        conn.close()


update(VDOPjs,'VDOP','1')
update(VDOPjs,'VDOP','2')
update(VDOPjs3,'VDOP','3')
update(HDOPjs,'HDOP','1')
update(HDOPjs,'HDOP','2')
update(HDOPjs3,'HDOP','3')
update(PDOPjs,'PDOP','1')
update(PDOPjs,'PDOP','2')
update(PDOPjs3,'PDOP','3')
update(GDOPjs,'GDOP','1')
update(GDOPjs,'GDOP','2')
update(GDOPjs3,'GDOP','3')
update(Rssjs,'RSS','1')
update(Rssjs,'RSS','2')
update(Rssjs3,'RSS','3')

