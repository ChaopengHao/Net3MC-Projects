# -*- coding: utf-8 -*-  
#!/usr/bin/env python

import wx  
import httplib
import json
import webbrowser


class StaticFlowPusher(object):
    def __init__(self,server):
        self.server=server
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
    def get(self, data):
        ret = self.rest_call(data, 'GET')
        return json.loads(ret[2])
    def remove(self,objtype,data):
        ret = self.rest_call(data, 'DELETE')
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


class DelFlowFrame(wx.Frame):  #删除流表
    ControllerIP='wew'
    def __init__(self,parent,title):  
        wx.Frame.__init__(self,parent,title=title,size=(320,130))  
        self.InitUI()  
        self.Centre()  
        self.Show()  
    def InitUI(self):  
        panel = wx.Panel(self)  
        sizer = wx.GridBagSizer(4,4)  
          
        text = wx.StaticText(panel,label='要删除的流表')  
        sizer.Add(text,pos=(0,1),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=5)  
          
        self.tc = wx.TextCtrl(panel)  

        sizer.Add(self.tc,pos=(1,1),span=(1,5),flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=5)  
          
        buttonConfirm = wx.Button(panel,label='确定',size=(90,28))  
        buttonCancel = wx.Button(panel,label='取消',size=(90,28))
        self.Bind(wx.EVT_BUTTON, self.confirm, buttonConfirm)
        self.Bind(wx.EVT_BUTTON, self.cancel, buttonCancel)  
        sizer.Add(buttonConfirm,pos=(3,3)) 
 
        sizer.Add(buttonCancel,pos=(3,4),flag=wx.RIGHT|wx.BOTTOM,border=5)  
          
        sizer.AddGrowableRow(2)  
        sizer.AddGrowableCol(1)  
        panel.SetSizerAndFit(sizer) 

    def confirm(self,event):
        data = self.tc.GetValue()
        pusher = StaticFlowPusher(str(Example.ControllerIP))
        pusher.remove(None,data)
    def cancel(self,event):
        self.Close() 


class AddFlowFrame(wx.Frame):  #添加流表的界面
    def __init__(self,parent,title):  
        wx.Frame.__init__(self,parent,title=title,size=(300,310))  
        self.InitUI()  
        self.Centre()  
        self.Show()  
    def InitUI(self):  
        panel = wx.Panel(self)  
        hbox = wx.BoxSizer(wx.HORIZONTAL)  
        fgs = wx.FlexGridSizer(10,2)  
          
        switch = wx.StaticText(panel,label='Switch:')  
        name = wx.StaticText(panel,label='Name:')  
        cookie = wx.StaticText(panel,label='Cookie')  
        priority = wx.StaticText(panel,label='Priority')
        in_port = wx.StaticText(panel,label='In_port')  
        active = wx.StaticText(panel,label='Active')
        eth_src = wx.StaticText(panel,label='Eth_src')  
        eth_dst = wx.StaticText(panel,label='Eth_dst')
        hard_timeout = wx.StaticText(panel,label='Hard_timeout')  
        actions = wx.StaticText(panel,label='Actions')

        buttonConfirm = wx.Button(panel,label='确定',size=(90,28))  
        buttonCancel = wx.Button(panel,label='取消',size=(90,28))
        self.Bind(wx.EVT_BUTTON, self.confirm, buttonConfirm)
        self.Bind(wx.EVT_BUTTON, self.cancel, buttonCancel) 
   
        self.switch1 = wx.TextCtrl(panel)  
        self.name1 = wx.TextCtrl(panel) 
        self.cookie1 = wx.TextCtrl(panel,value='0') 
        self.priority1 = wx.TextCtrl(panel,value='32767') 
        self.in_port1 = wx.TextCtrl(panel) 
        self.active1 = wx.TextCtrl(panel,value='true') 
        self.eth_src1 = wx.TextCtrl(panel) 
        self.eth_dst1 = wx.TextCtrl(panel) 
        self.hard_timeout1 = wx.TextCtrl(panel,value='0') 
        self.actions1 = wx.TextCtrl(panel)  
          
        fgs.AddMany([(switch),(self.switch1,1,wx.EXPAND),(name), (self.name1,1,wx.EXPAND),(cookie),  
                     (self.cookie1,1,wx.EXPAND),(priority), (self.priority1,1,wx.EXPAND),(in_port),  
                     (self.in_port1,1,wx.EXPAND),(active), (self.active1,1,wx.EXPAND),(eth_src),  
                     (self.eth_src1,1,wx.EXPAND),(eth_dst),  
                     (self.eth_dst1,1,wx.EXPAND),(hard_timeout),  
                     (self.hard_timeout1,1,wx.EXPAND),(actions,1,wx.EXPAND),           (self.actions1,1,wx.EXPAND),(buttonConfirm),(buttonCancel)])  
          
        fgs.AddGrowableCol(1,1)     
        hbox.Add(fgs,proportion=1,flag=wx.ALL|wx.EXPAND,border=15)  
        panel.SetSizer(hbox) 

    def cancel(self,event):
        self.Close()
    def confirm(self,event):
        flow={
         'switch':"%s"%str(self.switch1.GetValue()),
         "name":"%s"%str(self.name1.GetValue()),
         "cookie":"%s"%str(self.cookie1.GetValue()),
         "priority":"%s"%str(self.priority1.GetValue()),
         "eth_src" :"%s"%str(self.eth_src1.GetValue()),
         "in_port":"%s"%str(self.in_port1.GetValue()),
         "eth_dst" :"%s"%str(self.eth_dst1.GetValue()),
         "active":"%s"%str(self.active1.GetValue()),
         "actions":"%s"%str(self.actions1.GetValue()),
         "hard_timeout":"%s"%str(self.hard_timeout1.GetValue())
         }
        """flow2 = {     #测试所用
         'switch':"00:00:00:00:00:00:00:01",
          "name":"flow-mod-2",
          "cookie":"0",
          "priority":"32768",
          "in-port":"2",
          "active":"true",
          "actions":"output=flood"
        }"""
        #print str(Example.ControllerIP)
        pusher = StaticFlowPusher(str(Example.ControllerIP))
        pusher.set(flow) 
        #print flow

class GetFlowFrame(wx.Frame):   #获得流表界面
    def __init__(self,parent,title):  
        wx.Frame.__init__(self,parent,title=title,size=(320,130))  
        self.InitUI()  
        self.Centre()  
        self.Show()  
    def InitUI(self):  
        bkg = wx.Panel(self)  
        text = wx.StaticText(bkg,label='流表如下') 
 
        contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL) 
        pusher = StaticFlowPusher(str(Example.ControllerIP))
        #print str(pusher.get({}))
        #contents.SetValue(Example.pusher.get
        contents.SetValue(str(pusher.get({})))  
        hbox=wx.BoxSizer()  
        hbox.Add(text, proportion=0, flag=wx.LEFT, border=5)  
        vbox = wx.BoxSizer(wx.VERTICAL)  
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)  
        vbox.Add(contents, proportion=1,  
        flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)  
        bkg.SetSizer(vbox)

class Example(wx.Frame):  #初始界面
    ControllerIP='wew'
    def __init__(self,parent,title):  
        wx.Frame.__init__(self,parent,title=title,size=(320,130))  
        self.InitUI()  
        self.Centre()  
        self.Show()  
    def InitUI(self):  
        panel = wx.Panel(self)  
        sizer = wx.GridBagSizer(4,4)  
          
        text = wx.StaticText(panel,label='控制器的IP地址')  
        sizer.Add(text,pos=(0,1),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=5)  
          
        self.tc = wx.TextCtrl(panel)  

        sizer.Add(self.tc,pos=(1,1),span=(1,5),flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=5)  
          
        buttonConfirm = wx.Button(panel,label='确定',size=(90,28))  
        buttonCancel = wx.Button(panel,label='取消',size=(90,28))
        self.Bind(wx.EVT_BUTTON, self.confirm, buttonConfirm)
        self.Bind(wx.EVT_BUTTON, self.cancel, buttonCancel)  
        sizer.Add(buttonConfirm,pos=(3,3)) 
 
        sizer.Add(buttonCancel,pos=(3,4),flag=wx.RIGHT|wx.BOTTOM,border=5)  
          
        sizer.AddGrowableRow(2)  
        sizer.AddGrowableCol(1)  
        panel.SetSizerAndFit(sizer)  

    def confirm(self,event):
        Example.ControllerIP = self.tc.GetValue()
        Example.pusher=StaticFlowPusher(str(Example.ControllerIP))
        self.Close()
        frame1=Frame1(None,title='菜单界面')
        frame1.Show()
        #print Example.ControllerIP
    def cancel(self,event):
        self.Close()


class Frame1( wx.Frame ):   #选项界面
    def __init__(self,parent,title):  
        wx.Frame.__init__(self,parent,title=title,size=(300,100))  
        self.InitUI()  
        self.Centre()  
        self.Show()
    def InitUI(self):  
        panel = wx.Panel(self)  
        sizer = wx.GridBagSizer(3,3)  
          
        buttonAddFlow = wx.Button(panel,label='添加流表',size=(100,28))  
        buttonDelFlow = wx.Button(panel,label='删除流表',size=(100,28))
        buttonGetFlow = wx.Button(panel,label='获得流表',size=(100,28))  
        buttonGetTopo = wx.Button(panel,label='获得网络拓扑',size=(100,28))
        self.Bind(wx.EVT_BUTTON, self.addflow, buttonAddFlow)
        self.Bind(wx.EVT_BUTTON, self.delflow, buttonDelFlow)
        self.Bind(wx.EVT_BUTTON, self.getflow, buttonGetFlow)
        self.Bind(wx.EVT_BUTTON, self.gettopo, buttonGetTopo)  
        sizer.Add(buttonAddFlow,pos=(1,1)) 
        sizer.Add(buttonDelFlow,pos=(2,1))
        sizer.Add(buttonGetFlow,pos=(1,2)) 
        sizer.Add(buttonGetTopo,pos=(2,2)) 
        panel.SetSizerAndFit(sizer) 
    def addflow(self,event):
        addflowframe=AddFlowFrame(None,title='添加流表')
        addflowframe.Show()
    def delflow(self,event):
        delflow=DelFlowFrame(None,title='删除流表')
        delflow.Show()
    def getflow(self,event):
        getflow=GetFlowFrame(None,title='获得流表')
        getflow.Show()
    def gettopo(self,event):
        url = 'http://localhost:8080/ui/index.html'
        webbrowser.open(url)





if __name__ == '__main__':  
    app = wx.App()  
    Example(None,title='主界面')  
    app.MainLoop()  
