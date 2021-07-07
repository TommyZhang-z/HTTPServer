"""
HTTPServer部分的主程序

获取Http请求
解析Http请求
将请求发给WebFrame
从WebFrame接收反馈数据
将数据组织为response格式发送给客户端

并发：多线程并发
"""


from socket import *
import sys
from threading import Thread
from config import *
import re
import json


# 服务器地址
ADDR = (HOST, PORT)


# 将httpserver基本功能封装为类
class HTTPServer:
    def __init__(self):
        self.address = ADDR
        self.create_socket()
        self.bind()

    # 创建tcp套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.ip, self.port = self.address

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print(f"Listen to port: {self.port}")

        # 循环等待客户端连接
        while True:
            try:
                connfd, addr = self.sockfd.accept()
                print(f"Connect from:{addr}")
            except KeyboardInterrupt:
                sys.exit("Server Exit")
            except Exception as e:
                print(e)
                continue

            # 接收到客户端连接 开始线程
            ClientThread = Thread(target=self.handle, args=(connfd,))
            ClientThread.setDaemon(True)
            ClientThread.start()

    def handle(self, connfd):
        request = connfd.recv(4096).decode()
        # print(request)
        pattern = r'(?P<method>[A-Z]+)\s(?P<info>/\S*)'
        try:
            result = re.match(pattern, request).groupdict()
        except:
            connfd.close()
            return
        else:
            print(result)


httpd = HTTPServer()
httpd.server_forever()