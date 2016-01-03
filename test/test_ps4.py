from bs4 import BeautifulSoup
import re

html_doc = '<a href="https://www.baidu.com">百度</a><a href="https://www.google.com">Google</a><a href="https://www.test.com">test</a><p class="title">It is title!</p>'
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
print('获取所有的链接')

links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())

print('获取google的链接')
link_node=soup.find('a',href="https://www.google.com")
print(link_node.name, link_node['href'], link_node.get_text())


print('正则匹配')
link_node=soup.find('a',href=re.compile(r"tes"))
print(link_node.name, link_node['href'], link_node.get_text())

print('p段落')
p_node=soup.find('p',class_="title")
print(p_node.name, p_node.get_text())