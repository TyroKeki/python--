import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts
import 快速添加省市

f = open(r"C:\Users\13726\Desktop\python课件\黑马程序员\资料\可视化案例数据\地图数据\疫情.txt","r",encoding="utf-8")
data = f.read()
f.close()
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append([province_name, province_confirm])
# print(data_list)

for province_list in data_list:
    province_name = province_list[0]
    province_name = 快速添加省市.get_full_province_name(province_name)
    province_list[0] = province_name
# print(data_list)

map = Map()
map.add("各省份确诊人数",data_list,"china")

map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts = VisualMapOpts(is_show=True)

)

map.render("全国疫情图.html")
