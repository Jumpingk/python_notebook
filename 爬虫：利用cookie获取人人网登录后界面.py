from urllib import request, parse
from http import cookiejar

# 创建一个cookie实例
cookie = cookiejar.CookieJar()
# 创建cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http的管理器
http_handler = request.HTTPHandler()
# 创建https的管理器
https_handler = request.HTTPSHandler()
# # 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    url = 'http://www.renren.com/PLogin.do'
    '''
    登录人人网
    :return: 
    '''
    data = {
        'email': 'xxxxxxxx',  # 个人邮箱或手机号
        'password': 'xxxxxx'  # 个人密码
    }
    # 对数据进行编码
    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data)
    rsp = opener.open(req)


def getHome():
    url = 'http://www.renren.com/xxxxxx/profile'  # 登录后个人的主页网址
    rsp = opener.open(url)
    html = rsp.read().decode('utf-8')
    print(html)


if __name__ == '__main__':
    login()
    getHome()
