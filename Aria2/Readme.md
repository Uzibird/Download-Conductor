Aria2 模块：

1. [x] aria2.methods
   1. [x] add
   2. [x] tasks ( tellActive & getGlobalStat
   3. [x] remove (from downloading
   4. [x] clear ( purge/remove DownloadResult
   5. [x] pause ( single & all
   6. [x] tellWaiting
   7. [x] tellStopped
2. [x] 模块 打包

---

```
使用 jsonRpc 控制 aria2。(http://aria2.github.io/manual/en/html/aria2c.html)

# 实例化
a2 = aria2('http://ip:port/jsonrpc','token')
# 使用add方法 添加下载链接，dir为None时aria2会使用默认下载位置
a2.add([(url,dir)])

使用requests.post，正常返回格式为json ，需自行catch异常（timeout = 5）.
```