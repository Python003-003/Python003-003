import requests
import lxml.etree
import pandas as pd
url = "https://movie.douban.com/subject/1292052/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
header = {"user-agent": user_agent}
re = requests.get(url, headers=header)
# xml初始化数据
selector = lxml.etree.HTML(re.text)
# 获取xpath的对应的值
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print("电影名字：{0}".format(film_name))

plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print('电影上线的日期：{0}'.format(plan_date))


rating = selector.xpath('//*[@id="interest_sectl"\
    ]/div[1]/div[2]/strong/text()')
print('电影的评分：{0}'.format(rating))

mylist = [film_name, plan_date, rating]
movie1 = pd.DataFrame(data=mylist)
movie1.to_csv('./week01/movie\
    1.csv', encoding='utf8', index=False, header=False)
