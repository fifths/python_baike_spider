import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

values = {
    'wd': '啊',
    'ptype':'char'
}
data = urllib.parse.urlencode(values)
new_url = "http://dict.baidu.com/s?" + data+'#'

response = urllib.request.urlopen(new_url)
if response.getcode() != 200:
    print('faild')
else:
    print('success')
    html_cont = response.read()
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

    pinyin_node = soup.find('div', class_="pronounce").find_all('span')

    for pinyin in pinyin_node:
        pinyinInfo=pinyin.get_text()
        pinyinVoice=pinyin.a['url']
        print(pinyinInfo)
        print(pinyinVoice)

    header = soup.find(id="header-img").img['src']
    radical = soup.find(id="header-list").find(id='radical').find('span').get_text()#部 首
    traditional = soup.find(id="header-list").find(id='traditional').find('span').get_text()#部 首
    stroke_order = soup.find(id="header-list").find(id='stroke_order').find('span').get_text()#笔顺


    wubi=soup.find(id="wubi").find('span').get_text()#五笔
    sijiao = soup.find(id="sijiao").find('span').get_text()#四角
    cangjie = soup.find(id="cangjie").find('span').get_text()#仓颉
    line_type = soup.find(id="line_type").find('span').get_text()#五行
    stroke_count = soup.find(id="stroke_count").find('span').get_text()#笔画数
    zheng_code = soup.find(id="zheng_code").find('span').get_text()#郑码
    struct_type = soup.find(id="struct_type").find('span').get_text()#字结构
    rough_comp = soup.find(id="rough_comp").find('span').get_text()#部件拆解
    pronunciation = soup.find(id="pronunciation").find('span').get_text()#注音
    variants= soup.find(id="variants").find('span').get_text()# 异体字
    unicode= soup.find(id="unicode").find('span').get_text()#统一码

    infos = soup.find("div",class_="tab-content").find('dl')


    print(header)
    print(radical)
    print(traditional)
    print(stroke_order)

    print(wubi)
    print(sijiao)
    print(cangjie)
    print(line_type)
    print(stroke_count)
    print(zheng_code)
    print(struct_type)
    print(rough_comp)
    print(pronunciation)
    print(variants)
    print(unicode)
    print(infos)

    print(traditional)

#traditional
    #


        #print(pinyin)
    #print(pinyin_node)
    #res_data['title'] = title_node.get_text()
    #fout = open('output.html', 'wb')
    #fout.write(html_cont)
    #fout.close()
