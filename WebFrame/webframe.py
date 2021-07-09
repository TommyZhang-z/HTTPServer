"""
webframe.py 模拟后端应用工作流程
"""
import sys
from socket import *
from select import select
import json
from settings import *
from urls import *


# 应用类，处理某一方面的请求
class Application:

    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.msg = {}
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind((FRAME_IP, FRAME_PORT))

    def start(self):
        self.sockfd.listen(3)
        print(f"Listen to port:{FRAME_PORT}")
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            self.receive(rs)
            self.responding(ws)

    def responding(self, ws):
        for w in ws:
            w.send((self.msg[w]).encode())
            del self.msg[w]
            self.wlist.remove(w)

    def receive(self, rs):
        for r in rs:
            if r is self.sockfd:
                connfd, addr = r.accept()
                self.rlist.append(connfd)
            else:
                self.handle(r)
                self.rlist.remove(r)

    def handle(self, connfd):
        data = connfd.recv(1024).decode()
        data = json.loads(data)
        print(data)
        if data['method'] == 'GET':
            if data['info'] == '/' or data['info'][-5:] == '.html':
                response = self.get_html(data['info'])
            else:
                response = self.get_data(data['info'])
        elif data['method'] == 'POST':
            pass
        self.msg[connfd] = json.dumps(response)
        self.wlist.append(connfd)

    def get_html(self, info) -> dict:
        if info == "/":
            filename = Directory + "/index.html"
        else:
            filename = Directory + info
        try:
            fd = open(filename, 'r', encoding='utf-8')
        except:
            fd = open(Directory + '/404.html', 'r', encoding='utf-8')
            return {"status": "404", 'data': fd.read()}
        else:
            return {"status": "200", 'data': fd.read()}

    def get_data(self, info):
        # 规定格式
        for url, func in urls:
            if url == info:
                return {'status': '200', 'data': func()}
        return {'status': '404', 'data': 'Sorry...'}

        # 我自己的处理方法
        # if info in urls:
        #     return {'status': '200', 'data': urls[info]()}
        # else:
        #     return {'status': '200', 'data': 'Sorry...'}


app = Application()
app.start()
