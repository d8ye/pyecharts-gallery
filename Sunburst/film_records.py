import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Sunburst
from pyecharts.commons.utils import JsCode

"""
Gallery 使用 pyecharts 1.3.1
参考地址: https://echarts.baidu.com/examples/editor.html?c=sunburst-book

目前无法实现的功能:
暂无
"""

film_data = [{"分类":  "电影", "类型":  "喜剧", "评分":  "5☆", "名称":  "我不是药神"},
{"分类":  "电影", "类型":  "喜剧", "评分":  "4☆", "名称":  "无名之辈"},
{"分类":  "电影", "类型":  "喜剧", "评分":  "4☆", "名称":  "阿浪的远方"},
{"分类":  "电影", "类型":  "喜剧", "评分":  "3☆", "名称":  "一出好戏"},
{"分类":  "电影", "类型":  "剧情", "评分":  "5☆", "名称":  "无双"},
{"分类":  "电影", "类型":  "剧情", "评分":  "4☆", "名称":  "大象席地而坐"},
{"分类":  "电影", "类型":  "剧情", "评分":  "4☆", "名称":  "风中有朵雨做的云"},
{"分类":  "电影", "类型":  "剧情", "评分":  "4☆", "名称":  "过春天"},
{"分类":  "电影", "类型":  "剧情", "评分":  "3☆", "名称":  "无问东西"},
{"分类":  "电影", "类型":  "爱情", "评分":  "5☆", "名称":  "江湖儿女"},
{"分类":  "电影", "类型":  "爱情", "评分":  "4☆", "名称":  "地球最后的夜晚"},
{"分类":  "电影", "类型":  "爱情", "评分":  "4☆", "名称":  "你好之华"},
{"分类":  "电影", "类型":  "爱情", "评分":  "2☆", "名称":  "后来的我们"},
{"分类":  "电影", "类型":  "动作", "评分":  "4☆", "名称":  "红海行动"},
{"分类":  "电影", "类型":  "动作", "评分":  "4☆", "名称":  "影"},
{"分类":  "电影", "类型":  "动作", "评分":  "4☆", "名称":  "动物世界"},
{"分类":  "电影", "类型":  "动画", "评分":  "5☆", "名称":  "夜思"},
{"分类":  "电影", "类型":  "动画", "评分":  "4☆", "名称":  "切尔诺贝利之春"},
{"分类":  "电影", "类型":  "动画", "评分":  "4☆", "名称":  "女他"},
{"分类":  "电影", "类型":  "动画", "评分":  "3☆", "名称":  "风语咒"},
{"分类":  "电影", "类型":  "惊悚", "评分":  "4☆", "名称":  "灵魂摆渡·黄泉"},
{"分类":  "电影", "类型":  "武侠", "评分":  "3☆", "名称":  "夺命剑之风云再起"},
{"分类":  "电影", "类型":  "武侠", "评分":  "2☆", "名称":  "狄仁杰之四大天王"},
{"分类":  "电视剧", "类型":  "现代", "评分":  "5☆", "名称":  "大江大河"},
{"分类":  "电视剧", "类型":  "现代", "评分":  "5☆", "名称":  "疯人院"},
{"分类":  "电视剧", "类型":  "现代", "评分":  "5☆", "名称":  "天坑猎鹰"},
{"分类":  "电视剧", "类型":  "现代", "评分":  "4☆", "名称":  "SCI迷案集"},
{"分类":  "电视剧", "类型":  "现代", "评分":  "4☆", "名称":  "古董中情局"},
{"分类":  "电视剧", "类型":  "现代", "评分":  "4☆", "名称":  "乡村爱情协奏曲"},
{"分类":  "电视剧", "类型":  "现代", "评分":  "3☆", "名称":  "上海女子图鉴"},
{"分类":  "电视剧", "类型":  "古装", "评分":  "5☆", "名称":  "天盛长歌"},
{"分类":  "电视剧", "类型":  "古装", "评分":  "4☆", "名称":  "小戏骨：水浒传"},
{"分类":  "电视剧", "类型":  "古装", "评分":  "4☆", "名称":  "香蜜沉沉烬如霜"},
{"分类":  "电视剧", "类型":  "古装", "评分":  "3☆", "名称":  "知否知否应是绿肥红瘦"}]


film_dataframe = pd.DataFrame(film_data, columns=['分类', '类型', '评分', '名称'])
colors = ['#FFAE57', '#FF7853', '#EA5151', '#CC3F57', '#9A2555', '#2E2733']

def tree_data(data, colors):
    result = []
    star_color = {}
    #设置评分的颜色
    for i, j in enumerate(data.iloc[:,2].unique(),1):
        star_color[j] = colors[i]
    #第一次遍历，得到第一层目录
    for i in data.iterrows():
        dic = {}
        dic['name'] = i[1][data.columns[0]]
        dic['children'] = []
        if dic not in result:
            result.append(dic)
    #第二次遍历，添加第二层目录
    for i in data.iterrows():
        dic = {}
        dic['name'] = i[1][data.columns[1]]
        dic['children'] = []
        for k in result:
            if (k['name'] == i[1][data.columns[0]]) and (dic not in k['children']):
                k['children'].append(dic)
    #第三次遍历，添加第三层目录
    for i in data.iterrows():
        dic = {}
        dic['name'] = i[1]['评分']
        dic['children'] = []
        for k in result:
            for m in k['children']:
                if (k['name'] == i[1][data.columns[0]]) and (m['name'] == i[1][data.columns[1]]) and (dic not in m['children']):
                    m['children'].append(dic)
    #第四次遍历，添加子元素，添加各元素的颜色代码
    for i in data.iterrows():
        dic = {}
        dic['name'] = i[1]['名称']
        dic['value'] = 1
        for num, k in enumerate(result, 1):
            k['itemStyle'] = {'color': colors[num]}
            for m in k['children']:
                m['itemStyle'] = {'color': colors[num]}
                for n in m['children']:
                    n['label'] = {'color': star_color[n['name']]}
                    if ((k['name'] == i[1][data.columns[0]]) and (m['name'] == i[1][data.columns[1]])
                    and (n['name'] == i[1][data.columns[2]])):
                        dic['itemStyle'] = {'color': star_color[n['name']]}
                        dic['label'] = {'color': star_color[n['name']]}
                        n['children'].append(dic)
    return result


def sunburst(data) -> Sunburst:
    c = (
        Sunburst(init_opts=opts.InitOpts(width="900px", height="900px", bg_color=colors[-1]))
        .add(
            "",
            data_pair=data,
            highlight_policy='descendant',
            label_opts=opts.LabelOpts(rotate='radial', font_size=14, color=colors[-1]),
            itemstyle_opts=opts.ItemStyleOpts(border_color=colors[-1], border_width=2),
            sort_=JsCode("""function (a, b){
                        if (a.depth <= 2){
                            return b.getValue() - a.getValue();
                        }
                        else{
                            return b.dataIndex - a.dataIndex;
                        }
                    }"""),
            levels=[
                {},
                {
                    'r0': '0',
                    'r': '60',
                    'label': {'rotate': '0'}
                },
                {
                    'r0': '60',
                    'r': '160'
                },
                {
                    'r0': '175',
                    'r': '210',
                    'itemStyle': {'shadowBlur': '2', 'shadowColor': colors[2], 'color': 'transparent'},
                    'label': {'rotate': 'tangential', 'fontSize': '12'}
                },
                {
                    'r0': '210',
                    'r': '215',
                    'itemStyle': {'shadowBlur': '80', 'shadowColor': colors[0]},
                    'label': {'position': 'outside', 'textShadowBlur': '5', 'textShadowColor': '#333'},
                    'downplay': {'label': {'opacity': '0.2'}}
                }
            ]
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Film_records_Sunburst",
                                                   title_textstyle_opts=opts.TextStyleOpts(
                                                       color=colors[-2]
                                                   )
                        )
        )
    )
    return c

sunburst(tree_data(film_dataframe, colors)).render('film_sunburst.html')