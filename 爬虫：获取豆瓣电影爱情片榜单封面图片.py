from urllib import request
import json
import time
import random
'''
项目：爬取豆瓣爱情片电影封面
'''


class douban_love_moives():

    def __init__(self, k):
        self.k = k

    def load_moive(self, start):
        url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=' + str(
            start) + '&limit=20'
        time.sleep(random.randint(1, 4))
        rsp = request.urlopen(url)
        json_data = json.loads(rsp.read().decode())

        for moive in json_data:
            self.k += 1
            time.sleep(random.randint(2, 5))
            try:
                request.urlretrieve(moive['cover_url'], 'F:\文件存放处\爱情片电影封面\\' + moive['title'] + '.jpg')
                print('第' + str(self.k) + '张图片下载成功：' + moive['cover_url'])
            except Exception:
                print('第' + str(self.k) + '张图片下载失败：' + moive['cover_url'])

    def get_moives(self):
        for start in range(0, 351, 20):

            # 使用代理步骤
            # - 1、设置代理地址
            proxys = [{'http': '39.137.69.10:8080'},
                    {'http': '60.255.186.169:8888'},
                    {'http': '117.191.11.108:80'}]
            # - 2、创建ProxyHandler
            proxy = random.choice(proxys)
            proxy_handler = request.ProxyHandler(proxy)
            # - 3、创建Opener
            opener = request.build_opener(proxy_handler)
            # - 4、导入Opener
            request.install_opener(opener)
            self.load_moive(self.k)


if __name__ == '__main__':
    print('开始下载图片......')
    moive = douban_love_moives(k=0)
    moive.get_moives()



