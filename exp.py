import MySQLdb
import string
import csv


def up_element_array(arr):
    arr.append(arr[:-1]+1)
    return (arr[:-1])


def constuct_array_id(arg, arr_id):
    if (arg in arr_id):
        pass
    else:
        arr_id.append(arg)
    return (arr_id)


# arr_options
arr = []
# arr_id = [[1 for j in range(1)] for i in range(21)]  https://svyazhisama.ru/catalog/view/javascript/bootstrap/css/bootstrap.min.css  "class="example_beauty"
arr_id = []
for x in range(0, 22):
    arr_id.append([])

db = MySQLdb.connect(
    host="54.38.176.15",
    user="furni",
    passwd="svg#SD201",
    db="furni",
    charset='utf8')

cursor = db.cursor()


sql = "SELECT * FROM `oc_option_value` ORDER BY `oc_option_value`.`option_id` "
cursor.execute(sql)
sql = "SELECT * FROM `oc_option_value`"  # WHERE `quantity` > 100 "

cursor.execute(sql)


data = cursor.fetchall()

for rec in data:
    
    name = rec
    opt_id = int(name[1])
    sort_num = int(name[3])
    
    if len(arr_id[opt_id]) == 0:
        arr_id[opt_id].append(0)
    
    else:
        sort = arr_id[opt_id][-1]+1
        arr_id[opt_id].append(sort)
    
    print('id ', opt_id, '   ',  arr_id[opt_id])

cursor.close()
db.close()
