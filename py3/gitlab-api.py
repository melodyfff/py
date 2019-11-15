# coding=utf-8
# 提取gitlab的forks用户数量
# 依赖 ： pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple BeautifulSoup4
import urllib.request
from bs4 import BeautifulSoup
import re


def url_open(url, time=20):  # 打开网页如： https://gitlab.com/fdroid/fdroidclient/-/forks?page=1
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/78.0.3904.97 Safari/537.36')
    req.add_header('Cookie',
                   '_mkto_trk=id:194-VVC-221&token:_mch-gitlab.com-1504792645202-45229; '
                   'optimizelyEndUserId=oeu1519739829496r0.4762679017271554; _ga=GA1.2.1205164215.1504792644; '
                   '_biz_uid=b8c35c1dac174ca8c3be6cc70c8491b2; '
                   '_biz_flagsA=%7B%22Version%22%3A1%2C%22XDomain%22%3A%221%22%7D; sidebar_collapsed=true; '
                   'frequently_used_emojis=flushed; _gid=GA1.2.577034924.1573732442; '
                   '_hjid=319bb520-2f4b-41f9-bb0a-93ba8324232a; '
                   'experimentation_subject_id=ImFiNGM3NzFjLTgwNjQtNDA0NS05NjMwLWRiN2ZmZDAxNmVjZSI%3D'
                   '--2ee2cd60f0a31075d1b9879a4e7ed1eca6f3250e; event_filter=all; '
                   '_gitlab_session=ed72896f8bd686e90b48e5f383f4f52a; _biz_nA=11; _biz_pendingA=%5B%5D; '
                   '_sp_id.6b85=943612f0-695c-4413-937b-ae3e2fdebf57.1545574812.8.1573733600.1546704064.dbd2e18e-cccf'
                   '-409d-895b-c6916a5cfe51111')
    req.add_header('Host', 'gitlab.com')

    response = urllib.request.urlopen(url, timeout=time)
    html = response.read().decode("utf-8")
    return html


def save_html(html, file_path='hello.html'):  # 将网页写入本地
    with open(file_path, 'w+', encoding='utf-8') as file:
        for line in html:
            file.write(line)
    print("write to [%s] down" % file_path)


def total_page(html):  # 获取总页数
    soup = BeautifulSoup(html, 'lxml')
    total = int(re.findall(r"\d+\.?\d*", soup.select('.js-last-button > a')[0]['href'])[0])
    print("Pages [%d]" % total)
    return total


def analysis_html(html):  # 解析页面，提取用户名
    soup = BeautifulSoup(html, 'lxml')
    print("Title [%s]" % soup.title)
    print("Title [%s]" % soup.title.string)

    names = soup.find_all('span', class_="namespace-name")
    for name in names:
        print(name.string.replace("/", "").strip())  # 去除回车和空格


def get_total_page_list(html):
    pages = []
    total = total_page(html)
    while total > 0:
        pages.append('https://gitlab.com/fdroid/fdroidclient/-/forks?page=' + str(total))
        total -= 1
    print(pages)
    return pages


# save_html(url_open('https://gitlab.com/fdroid/fdroidclient/-/forks?page=1'))  # 打开网页并保存到本地
total_page(open('hello.html', 'r', encoding='utf-8'))  # 统计总页数
get_total_page_list(open('hello.html', 'r', encoding='utf-8'))  # 获取请求列表
analysis_html(open('hello.html', 'r', encoding='utf-8'))  # 读取本地文件调试
