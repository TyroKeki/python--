from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pymysql import Connection

tfr = TextFileReader("./2011年1月销售数据.txt")
jfr = JsonFileReader("./2011年2月销售数据JSON.txt")

jan_data = tfr.read_data() #type:list[Record]
feb_data = jfr.read_data() #type:list[Record]

all_data = jan_data + feb_data

# data_dict = {}
# for record in all_data:
#     if record.date in data_dict.keys():
#         data_dict[record.date] += record.money
#
#     else:
#         data_dict[record.date] = record.money
#
# # print(data_dict)
# bar = Bar(init_opts=InitOpts(theme=ThemeType.ROMANTIC))
# bar.add_xaxis(list(data_dict.keys()))
# bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
# bar.set_global_opts(
#     title_opts = TitleOpts(title="每日销售额")
# )
#
# bar.render("每日销售额.html")

# print(all_data)
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True,
)
cursor = conn.cursor()
conn.select_db("py_sql")
for record in all_data:
    sql = (f"insert into orders(order_date, order_id, money, province) "
           f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}') ")
    cursor.execute(sql)

sql = f"select * from orders"
cursor.execute(sql)
results = cursor.fetchall()
print(results)

conn.close()