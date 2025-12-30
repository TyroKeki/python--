import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts

f_us = open("D:/美国.txt",'r',encoding='utf-8')
us_data = f_us.read()
us_data = us_data.replace('jsonp_1629344292311_69436(','',1)
us_data = us_data[:-2:1]
us_dict = json.loads(us_data)
# print(type(us_dict))

trend_data = us_dict['data'][0]['trend']
# print(trend_data)

x_trend_data = trend_data['updateDate']
# print(x_trend_data)

us_x_data = x_trend_data[0:314]
# print(x_data)

us_y_data = trend_data['list'][0]['data'][0:314]
# print(y_data)
f_us.close()

'''日本'''
f_us = open("D:/日本.txt",'r',encoding='utf-8')
us_data = f_us.read()
us_data = us_data.replace('jsonp_1629350871167_29498(','',1)
us_data = us_data[:-2:1]
us_dict = json.loads(us_data)
# print(type(us_dict))

trend_data = us_dict['data'][0]['trend']
# print(trend_data)

x_trend_data = trend_data['updateDate']
# print(x_trend_data)

jp_x_data = x_trend_data[0:314]
# print(x_data)

jp_y_data = trend_data['list'][0]['data'][0:314]
# print(y_data)
f_us.close()

'''印度'''
f_us = open("D:/印度.txt",'r',encoding='utf-8')
us_data = f_us.read()
us_data = us_data.replace('jsonp_1629350745930_63180(','',1)
us_data = us_data[:-2:1]
us_dict = json.loads(us_data)
# print(type(us_dict))

trend_data = us_dict['data'][0]['trend']
# print(trend_data)

x_trend_data = trend_data['updateDate']
# print(x_trend_data)

in_x_data = x_trend_data[0:314]
# print(x_data)

in_y_data = trend_data['list'][0]['data'][0:314]
# print(y_data)
f_us.close()

# print(in_x_data, in_y_data)
# print(jp_x_data, jp_y_data)

line = Line()

line.add_xaxis(us_x_data) #共用日期
line.add_yaxis("美国确诊人数", us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data,label_opts=LabelOpts(is_show=False))


line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印对比折线图"),


)

line.render()