from bs4 import BeautifulSoup
import re

class HtmlParser(object):

    def paser(self, html_info):
        if html_info is None:
            return

        soup = BeautifulSoup(html_info, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(soup)
        return new_data

    def _get_new_data(self, soup):
        res_data = {
            'pinyin_node': [],#拼音
            'header': '',#字图片
            'radical': '',#部首
            'traditional': '',#繁体
            'stroke_order': '',#笔顺
            'wubi':'',# 五笔
            'sijiao':'',# 四角
            'cangjie':'',# 仓颉
            'line_type':'',# 五行
            'stroke_count':'',# 笔画数
            'zheng_code':'',# 郑码
            'struct_type':'',# 字结构
            'rough_comp':'',# 部件拆解
            'pronunciation':'',# 注音
            'variants':'', # 异体字
            'unicode':''# 统一码
        }
        pronounce = soup.find('div', class_="pronounce")
        if pronounce is not None:
            pinyin_node = pronounce.find_all('span')
            pinyinarray = {}
            for pinyin in pinyin_node:
                pinyinInfo = pinyin.get_text().strip()
                pinyinVoice = pinyin.a['url'].strip()
                pinyinarray[pinyinInfo] = pinyinVoice
            res_data['pinyin_node'] = pinyinarray

        headimg = soup.find(id="header-img")
        if headimg is not None:
            header = headimg.img['src'].strip()
            res_data['header'] = header

        headlist = soup.find(id="header-list")
        if headlist is not None:
            if headlist.find(id='radical') is not None:
                radical = headlist.find(id='radical').find('span').get_text().strip()  # 部 首
                res_data['radical'] = radical

            if headlist.find(id='traditional') is not None:
                traditional = headlist.find(id='traditional').find('span').get_text().strip()  # 繁体
                res_data['traditional'] = traditional

            if headlist.find(id='stroke_order') is not None:
                stroke_order = headlist.find(id='stroke_order').find('span').get_text().strip()  # 笔顺
                res_data['stroke_order'] = stroke_order

        if soup.find(id="wubi") is not None:
            wubi = soup.find(id="wubi").find('span').get_text().strip()  # 五笔
            res_data['wubi'] = wubi

        if soup.find(id="sijiao") is not None:
            sijiao = soup.find(id="sijiao").find('span').get_text().strip()  # 四角
            res_data['sijiao'] = sijiao

        if soup.find(id="cangjie") is not None:
            cangjie = soup.find(id="cangjie").find('span').get_text().strip()  # 仓颉
            res_data['cangjie'] = cangjie

        if soup.find(id="line_type") is not None:
            line_type = soup.find(id="line_type").find('span').get_text().strip()  # 五行
            res_data['line_type'] = line_type

        if soup.find(id="stroke_count") is not None:
            stroke_count = soup.find(id="stroke_count").find('span').get_text().strip()  # 笔画数
            res_data['stroke_count'] = stroke_count

        if soup.find(id="zheng_code") is not None:
            zheng_code = soup.find(id="zheng_code").find('span').get_text().strip()  # 郑码
            res_data['zheng_code'] = zheng_code

        if soup.find(id="struct_type") is not None:
            struct_type = soup.find(id="struct_type").find('span').get_text().strip()  # 字结构
            res_data['struct_type'] = struct_type

        if soup.find(id="rough_comp") is not None:
            rough_comp = soup.find(id="rough_comp").find('span').get_text().strip()  # 部件拆解
            res_data['rough_comp'] = rough_comp

        if soup.find(id="pronunciation") is not None:
            pronunciation = soup.find(id="pronunciation").find('span').get_text().strip()  # 注音
            res_data['pronunciation'] = pronunciation

        if soup.find(id="variants") is not None:
            variants = soup.find(id="variants").find('span').get_text().strip()  # 异体字
            res_data['variants'] = variants

        if soup.find(id="unicode") is not None:
            unicode = soup.find(id="unicode").find('span').get_text().strip()  # 统一码
            res_data['unicode'] = unicode

        if  soup.find("div", class_="tab-content") is not None:
            infos = soup.find("div", class_="tab-content").find_all('dl')
            content=[]
            for info in infos:
                print(info)
                pattern=re.compile(".")
                a=info.find(pattern)
                print(a)

            res_data['infos']=infos

        return res_data
