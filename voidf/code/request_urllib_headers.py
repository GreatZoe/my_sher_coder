import urllib.request
hds = {
    "User-Agent":'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    "host":'www.baidu.com'
}
req=urllib.request.Request('http://www.baidu.com',headers=hds)
resu = urllib.request.urlopen(req)
print(resu.read().decode("utf-8"))
