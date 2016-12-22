#encoding:utf-8

import httplib
import json

class StaticFlowPusher(object):
    def __init__(self,server):
        self.server=server
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
              'Content-type': 'application/json',
              'Accept': 'application/json',  
              }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret

pusher = StaticFlowPusher('192.168.56.1')

flow1 = {
     'switch':"00:00:00:00:00:00:00:03",
     "name":"flow1",
     "cookie":"0",
     "priority":"32766",
     "in_port":"1",
     "active":"true",
     "actions":"output=drop"
    }
flow2 = {
     'switch':"00:00:00:00:00:00:00:03",
     "name":"flow2",
     "cookie":"0",
     "priority":"32767",
     "in_port":"1",
     "eth_src" :"12:a1:18:32:d7:e9",
     "eth_dst" :"1e:a6:1d:4c:ea:cf",
     "active":"true",
     "actions":"output=2"
    }
flow3 = {
     'switch':"00:00:00:00:00:00:00:03",
     "name":"flow3",
     "cookie":"0",
     "priority":"32767",
     "in_port":"2",
     "eth_src" :"1e:a6:1d:4c:ea:cf",
     "eth_dst" :"12:a1:18:32:d7:e9",
     "active":"true",
     "actions":"output=1"
    }
flow4 = {
     'switch':"00:00:00:00:00:00:00:03",
     "name":"flow4",
     "cookie":"0",
     "priority":"32767",
     "in_port":"1",
     "eth_src" :"02:28:a3:68:94:b9",
     "eth_dst" :"1e:a6:1d:4c:ea:cf",
     "active":"true",
     "actions":"output=2"
    }
flow5 = {
     'switch':"00:00:00:00:00:00:00:03",
     "name":"flow5",
     "cookie":"0",
     "priority":"32767",
     "in_port":"2",
     "eth_src" :"1e:a6:1d:4c:ea:cf",
     "eth_dst" :"02:28:a3:68:94:b9",
     "active":"true",
     "actions":"output=1"
    }
a=raw_input('是否将用户1设置为代理用户：')
b=raw_input('是否将用户2设置为代理用户：')
if a=='y':
     pusher.set(flow2)
     pusher.set(flow3)
if b=='y':
     pusher.set(flow5)
     pusher.set(flow4)

pusher.set(flow1)
