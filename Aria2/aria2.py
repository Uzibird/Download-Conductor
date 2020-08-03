from json import dumps
from time import time
from requests import post

class aria2:
    
    def __init__(self, host, token,keys=None):
        self.host = host
        self.token = 'token:'+token if token else None
        self.keys = keys if keys else \
        ['gid', 'totalLength', 'completedLength','downloadSpeed', 'uploadSpeed', 'dir', 'files','connections','numSeeders']

    def _methods(self):
        params = [{'methodName':'system.listMethods'}]
        return self.post(params)

    def tasks(self):
        params = [
            {'methodName':'aria2.getGlobalStat','params':[self.token]},
            {'methodName':'aria2.tellActive','params':[self.token,self.keys]}
                ]
        return self.post(params)

    def add(self,Uris:list):
        params = []
        for url,path in Uris:
            if path:
                params.append({'methodName':'aria2.addUri','params':[self.token,[url],{'dir':path}]})
            else:
                params.append({'methodName':'aria2.addUri','params':[self.token,[url]]})

        return self.post(params)

    def rm(self,gids:list):
        params = []
        for gid in gids:
            
            params.append({'methodName':'aria2.remove','params':[self.token,gid]})
           
        return self.post(params)

    def waiting(self,offset,num):
        params = []
        params.append({'methodName':'aria2.tellWaiting','params':[self.token,offset,num,self.keys]})
        return self.post(params)

    def stopped(self,offset,num):
        params = []
        params.append({'methodName':'aria2.tellStopped','params':[self.token,offset,num,self.keys]})
        return self.post(params)

    def pause(self,gids:list):
        params = []
        for gid in gids:
            params.append({'methodName':'aria2.pause','params':[self.token,gid]})
        return self.post(params)

    def pauseAll(self):
        params = []
        params.append({'methodName':'aria2.pauseAll','params':[self.token]})
        return self.post(params)

    def clear(self,gids:list):
        params = []
        for gid in gids:
            params.append({'methodName':'aria2.removeDownloadResult','params':[self.token,gid]})
        return self.post(params)

    def clearAll(self):
        params = [{'methodName':'aria2.purgeDownloadResult','params':[self.token]}]
        return self.post(params)

    def post(self,params=None):
        data = {'jsonrpc': '2.0', 'id': 'Rin_'+str(time()),
               'method': 'system.multicall',
               'params': [params]
               }
        if not params:
            del data['params']
        result = post(self.host,data=dumps(data),headers={'Connection':'close'},timeout=5)
        return result

__all__ = ['']