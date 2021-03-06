
""" 
使用 jsonRpc 控制 aria2。(http://aria2.github.io/manual/en/html/aria2c.html)

# 实例化
a2 = aria2('http://ip:port/jsonrpc','token')
# 使用add方法 添加下载链接，dir为None时aria2会使用默认下载位置
a2.add([(url,dir)])

使用requests.post，正常返回格式为json ，需自行catch异常（timeout = 5）.
"""

from .aria2 import aria2