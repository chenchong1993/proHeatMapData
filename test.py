import pymysql.cursors
import json

# 阈值
WIFI_MAX = -20
WIFI_MIN = -90
BLUE_TOOTH_MAX = -20
BLUE_TOOTH_MIN = -90

# 全局lng判断重复变量
TMP_LNG = '0'


# 判断是否重复
def is_repeat(lng):
    # return False
    global TMP_LNG
    if (lng == TMP_LNG):
        return True
    TMP_LNG = lng;
    return False;


# 处理数据(根据阈值去掉相应的数据然后取平均)
def get_mean_and_detele_useless_data(min_num, max_num, data=[]):
    valid_num = 0
    accumulator = 0
    for item in data:
        print(data[item])
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

        # 重复则继续
        if (is_repeat(lng)):
            continue;

        wifi_val = get_mean_and_detele_useless_data(WIFI_MIN, WIFI_MAX, wifi_arr)

        blue_tooth_val = get_mean_and_detele_useless_data(BLUE_TOOTH_MIN, BLUE_TOOTH_MAX, blue_tooth_arr)

        target_arr.append([lng, lat, wifi_val, blue_tooth_val])

    return target_arr


# ------------------------------------main------------------------------------
# 连接数据库
connect = pymysql.Connect(
    host='121.28.103.199',
    port=5571,
    user='root',
    passwd='casmadmin2018',
    db='platformdata',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

startTime = '2018-10-22 00:00:00';
endTime = '2018-10-23 00:00:00';

# 查询数据
# sql = "SELECT * FROM obs WHERE created_at "
#
sql = " SELECT lng,lat,wifi,blue_tooth,sensor from obs WHERE created_at BETWEEN  '" + startTime + "'  and  '" + endTime + "' "
print(sql)

cursor.execute(sql)

print('共查找出', cursor.rowcount, '条数据')

arr = process_data(cursor.fetchall())

target_json = json.dumps(arr)

print(target_json)

# 关闭连接
cursor.close()
connect.close()