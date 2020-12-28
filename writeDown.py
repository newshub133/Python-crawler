# 导入库 json、urllib
import urllib.request
import json
# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}
# 发送请求获取数据
response = urllib.request.urlopen('https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7732190650992779231&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E4%B8%AD%E5%AD%A6%E7%94%9F+%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%AD%A6%E4%B9%A0&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E4%B8%AD%E5%AD%A6%E7%94%9F+%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%AD%A6%E4%B9%A0&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1609150399623=')
jsonStr = response.read().decode('utf-8')

# 分析数据提取链接
# 将json转换为字典
dict = json.loads(jsonStr)
num = 0
urllist = []
while num <30:
    url = dict['data'][num]['thumbURL']  # [0,29] 30张
    urllist.append(url)
    num = num+1

# 保存到excel
f = open('./herf.xls', 'w')
for href in urllist:
    f.write(href)
    f.writelines('\n')
f.close()
