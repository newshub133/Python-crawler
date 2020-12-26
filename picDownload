import urllib.request
import json
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


def req():
    response = urllib.request.urlopen('http://wallpaper.apc.360.cn/index.php?c=WallPaper&start=1&count=12&from=360chrome&a=getAppsByCategory&cid=26')  # 火狐浏览器
    json_data = response.read().decode('utf-8')
    print(json_data)
    return json_data


def analyse(data):
    dic_data = json.loads(data)   # json转词典
    print(dic_data['data'])
    urllist = []
    num = 0
    while num < 12:
        url = (dic_data['data'][num]['img_1600_900'])  # 提取出嵌套在字典里的链接 0-11, 12张图片
        num += 1
        urllist.append(url)
    print(urllist)
    return urllist


def download_pic(imglist):
    for img in imglist:
        name = random.randint(0, 100)
        urllib.request.urlretrieve(img, './pic/'+str(name)+'.png')
        print(str(name)+'.png'+'下载成功')


download_pic(analyse(req()))
