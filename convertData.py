import pymysql.cursors
import json
import csv


# 阈值
WIFI_MAX = -20
WIFI_MIN = -90
BLUE_TOOTH_MAX = -20
BLUE_TOOTH_MIN = -90

# 处理数据(根据阈值去掉相应的数据然后取平均)
def get_mean_and_detele_useless_data(min_num, max_num, data={}):
    valid_num = 0
    accumulator = 0
    for item in data:
        # print(data[item])
        val = int(data[item])
        if ((val < min_num) or (val > max_num) or (val == 0)):
            continue;
        valid_num = valid_num + 1;
        accumulator += val
    return accumulator / valid_num;


# 处理数据
def process_data(rows):
    target_arr = []

    for row in rows:
        # print(str(row) + '\n\n')
        lng = row[0]
        lat = row[1]
        wifi_arr = json.loads(row[2])
        blue_tooth_arr = json.loads(row[3])
        sensor_arr = json.loads(row[4])


        wifi_val = get_mean_and_detele_useless_data(WIFI_MIN, WIFI_MAX, wifi_arr)

        blue_tooth_val = get_mean_and_detele_useless_data(BLUE_TOOTH_MIN, BLUE_TOOTH_MAX, blue_tooth_arr)

        target_arr.append([lng, lat, wifi_val, blue_tooth_val])

    return target_arr


def loadcoo():
    f = open("coordmap.json", encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    text = json.load(f)
    return text
def loadwifi():
    f = open("wifiRMOne.json", encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    text = json.load(f)
    return text
def loadblu():
    f = open("bleRMOne.json", encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    text = json.load(f)
    return text
def csvToDic():
    csvtext = csv.reader(open("一楼坐标.csv"))
    # print(type(csvtext))
    cooBook={}
    for row in csvtext:
        cooBook[str(row[0])]=[float(row[1]),float(row[2])]
        # print(row)
    # print(cooBook)
    return cooBook

# ------------------------------------main------------------------------------

# coo = loadcoo()

wifi = loadwifi()
blu = loadblu()
coo = csvToDic()
point = []
f1Wifi = {}
f1Blu = {}
# print(coo)
# print(wifi)
#1-285
#286-626
#627-955

for item in range(955):
    # print(wifi[str(item+1)])
    for key in wifi[str(item+1)]:
        wifi_val = get_mean_and_detele_useless_data(WIFI_MIN, WIFI_MAX, wifi[str(item+1)])
        blue_tooth_val = get_mean_and_detele_useless_data(BLUE_TOOTH_MIN, BLUE_TOOTH_MAX, blu[str(item+1)])

    #     print(wifi[str(item+1)][key])
    #
    f1Wifi[item+1] = [coo[str(item+1)][1],coo[str(item+1)][0],wifi_val]
    f1Blu[item + 1] = [coo[str(item + 1)][1], coo[str(item + 1)][0], blue_tooth_val]

    # print(pointLine,',')
    # print(item+1,wifi_val,blue_tooth_val)
jsblu = json.dumps(f1Blu)
jswifi = json.dumps(f1Wifi)
print(jsblu)
print(jswifi)
