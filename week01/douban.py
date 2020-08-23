
import requests
from bs4 import BeautifulSoup as bs
url = "https://movie.douban.com/top250"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
header = {"user-agent": user_agent}
re = requests.get(url, headers=header)
bs_info = bs(re.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a',):
        # 获取所有链接
        print(atag.get('href'))
        # 获取电影名称
        print(atag.find('span',).text)
# print(re.text)
# print("返回码{0}".format(re.status_code))
