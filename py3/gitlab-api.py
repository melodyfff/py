# coding=utf-8

# 提取gitlab的forks用户数量
#
# 依赖 ： pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple BeautifulSoup4
#        pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple lxml
import urllib.request
from bs4 import BeautifulSoup
import re
import ssl
import time
from multiprocessing import Pool


def url_open(url, time_out=20):  # 打开网页如： https://gitlab.com/fdroid/fdroidclient/-/forks?page=1
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

    response = urllib.request.urlopen(url, timeout=time_out, context=ssl._create_unverified_context())  # 忽略ssl认证
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
    re_list = []
    soup = BeautifulSoup(html, 'lxml')
    # print("Title [%s]" % soup.title)  # 打印 title
    # print("Title [%s]" % soup.title.string) # 打印 title字符串https://gitlab.com/fdroid/fdroidclient

    names = soup.find_all('span', class_="namespace-name")
    for name in names:
        re_list.append(name.string.replace("/", "").strip())
        print(name.string.replace("/", "").strip())  # 去除回车和空格
    return re_list


def get_total_page_list(html):  # 获取访问页面列表
    pages = []
    total = total_page(html)
    while total > 0:
        pages.append('https://gitlab.com/fdroid/fdroidclient/-/forks?page=' + str(total))
        total -= 1
    print(pages)
    return pages


def test():  # 测试
    save_html(url_open('https://gitlab.com/fdroid/fdroidclient/-/forks?page=1'))  # 打开网页并保存到本地
    total_page(open('hello.html', 'r', encoding='utf-8'))  # 统计总页数
    get_total_page_list(open('hello.html', 'r', encoding='utf-8'))  # 获取请求列表
    analysis_html(open('hello.html', 'r', encoding='utf-8'))  # 读取本地文件调试


def multi(page_list):  # 多线程的方式
    p = Pool(10)
    r = []
    for page in page_list:
        r.append(p.apply_async(func=multi_analysis, args=(page,)))
    p.close()  # 关闭连接池,不再接收任务
    p.join()  # 等待任务执行完毕

    for res in r:  # 获取异步执行返回值
        result.extend(res.get())


def multi_analysis(url):
    return analysis_html(url_open(url))


def single(page_list):  # 单线程的方式
    for i in page_list:
        result.extend(analysis_html(url_open(i)))


if __name__ == '__main__':
    result = []
    print("获取fork数开始")
    start = time.time()
    req_list = get_total_page_list(url_open('https://gitlab.com/fdroid/fdroidclient/-/forks?page=1'))  # 获取请求列表
    multi(page_list=req_list)
    print("Total Cost : [%f] s" % (time.time() - start))
    print("Final Result: ", result)
    print("Final Total: ", len(result))
