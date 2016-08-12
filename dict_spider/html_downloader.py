import urllib.request
import urllib.parse
import urllib.error
import time
import os

class HtmlDownloader(object):
    def downloadbyword(self, url):
        if url is None:
            return None
        try:
            response = urllib.request.urlopen(url)
            if response.getcode() != 200:
                return None
        except urllib.error.HTTPError as e:
            #print(e.code)
            #print(e.read().decode("utf8"))
            return None

        return response.read()

    def downhead(self,root_url,header_url):
        headers = {
            'Accept': 'image/webp,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            'Referer': root_url,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',

        }
        req = urllib.request.Request(header_url, None, headers)
        try:
            response = urllib.request.urlopen(req)
            # print(response.read())
            filename=str(int(time.time()))
            fout = open('./img/'+filename+'.jpg', 'wb')
            fout.write(response.read())
            fout.close()
            return filename
        except urllib.error.HTTPError as e:
            #print(e.code)
            #print(e.read().decode("utf8"))
            return


    def downvoice(self, root_url, voice_url):
        headers = {
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            'Referer': root_url,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }
        req = urllib.request.Request(voice_url, None, headers)
        try:
            response = urllib.request.urlopen(req)
            filename = os.path.basename(voice_url)
            fout = open('./voice/' + filename, 'wb')
            fout.write(response.read())
            fout.close()
            return os.path.splitext(filename)[0]
            #return filename
        except urllib.error.HTTPError as e:
            # print(e.code)
            # print(e.read().decode("utf8"))
            return