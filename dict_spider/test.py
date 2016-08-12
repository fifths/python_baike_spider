import urllib.request
import urllib.parse
import urllib.error

url = 'http://dict.baidu.com/s?wd=%E5%95%8A&ptype=char'
img = 'http://t10.baidu.com/it/u=170101863,3577577251&fm=58'

headers = {
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',

}
req = urllib.request.Request(img, None,headers )

try:
    response = urllib.request.urlopen(req)
    #print(response.read())
    fout = open('output.jpg', 'wb')
    fout.write(response.read())
    fout.close()
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read().decode("utf8"))

##if response.getcode() != 200:
#    print('faild')
# else:
#    the_page = response.read()
#    print(the_page.decode("utf8"))
