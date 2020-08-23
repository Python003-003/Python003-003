import requests
from bs4 import BeautifulSoup as bs
url = tuple(f'https://movie.douban.com/top250?start={ page *25 }&\
    filter=' for page in range(0, 10))


# 函数功能是获取电影名和链接
def get_url(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    header = {"user-agent": user_agent}
    re = requests.get(url, headers=header)
    bs_info = bs(re.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a',):
            # 获取所有链接
            print(atag.get('href'))
            print(atag.find('span',).text)


if __name__ == "__main__":
    for i in url:
        get_url(i)
