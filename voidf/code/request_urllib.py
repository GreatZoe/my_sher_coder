import urllib.request

#请求百度网页
resu = urllib.request.urlopen('http://www.baidu.com')
print(resu.read())

#指定编码请求
with urllib.request.urlopen('http://www.baidu.com') as resu:
    print(resu.read(300).decode('GBK'))
    
#指定编码请求
f = urllib.request.urlopen('http://www.baidu.com')
print(f.read(100).decode('utf-8'))