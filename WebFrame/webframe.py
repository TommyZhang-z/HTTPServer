"""
webframe.py 模拟后端应用工作流程
"""
import sys
from socket import *
from select import select
import json
from settings import *


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

            for w in ws:
                w.send(json.dumps(self.msg[w]).encode())
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
        print(json.loads(data))
        self.msg[connfd] = {'status': '200', 'data': '<h1>HTTPServer 3.0 Arrived!</h1>'}
        self.wlist.append(connfd)


app = Application()
app.start()









