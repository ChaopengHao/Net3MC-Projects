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
     'switch':"00:00:00:00:00:00:00:01",
     "name":"flow1",
     "cookie":"0",
     "priority":"32767",
     "src-mac" :"00:00:00:00:00:01",
     "dst-mac" :"00:00:00:00:00:02",
     "active":"true",
     "actions":"output=drop",
     "hard_timeout":"60",
    }



pusher.set(flow1)
