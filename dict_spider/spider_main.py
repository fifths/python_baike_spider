import html_downloader
import html_parser
import urllib.parse

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()

    def craw(self, root_url):
        html_info = self.downloader.downloadbyword(root_url)
        new_data = self.parser.paser(html_info)
        if new_data['header'] !='':
            new_data['header_filename']=self.downloader.downhead(root_url,new_data['header'])

        pinyins={}
        if len(new_data['pinyin_node'])>0:
            for pinyin in new_data['pinyin_node']:
                filename=self.downloader.downvoice(root_url, new_data['pinyin_node'][pinyin])
                pinyins[pinyin] =filename

        new_data['pinyin']=pinyins
        print(new_data)





if __name__ == '__main__':
    word='啊'
    values = {
        'wd': word,
        'ptype': 'char'
    }
    data = urllib.parse.urlencode(values)
    root_url = "http://dict.baidu.com/s?" + data + '#'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)