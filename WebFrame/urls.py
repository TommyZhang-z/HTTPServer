"""
路由表
可以接受客户端什么样的数据访问
"""
from views import *


# 规定格式
urls = [
    ('/time', show_time),
    ('/hello', hello),
    ('/bye', bye)
]

# 我觉得效率高的字典格式
# urls = {
#     '/time': show_time,
#     '/hello': hello,
#     '/bye': bye
# }
