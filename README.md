Dakada是一个由dakada制作的网页框架，WSGI基于python内部库wsgiref，它学习了flask，支持基础web开发，以及数据库（数据存放在后缀为`.json`的文件中）、后台制作、cookie（遵循`{"key":"value"}`格式）、自行处理静态文件、蓝图（类似Flask的Blueprint）等功能，有自己的纠错功能，模板上引擎基于Jinja2，可自制过滤器，还支持用户注册、登录、登出以及webscoket等扩展功能


***

# 快速开始


首先，下载Dakada(pip install Dakada)，用`import dakada`导入Dakada


然后，在你的Dakada项目根目录下，运行指令`python -m dakada.startproject`


可在你的项目根目录下看到这几个文件：


![](https://asset.gitblock.cn/Media?name=8BDE3D49C34841DF12199B01614CD1DE.png)


`db`:数据库文件存储地


`staic`:静态文件存储地，Dakada会自动处理他们，比如你在staic里面放入一个叫`1.js`的文件，启动项目后，访问该文件链接为`/1.js`


`templates`:模板存储地





`cookies.txt`:存储所有用户的cookies，使所有cookies有了一定的安全性


`debug.txt`:报错日志

`webapp.py`:主程序


***

# Dakada的用法

~~~
# 基础开发
# from dakada import Dakada
class Dakada:
    def __init__(self,link=".",host='',port=8000):
        # 新建一个webapp
        # [link]项目根目录，默认值为当前目录
        # [host]IP地址，默认为本机
        # [port]端口，默认为8000
    def addpath(self,path,URL_type="URL",method=['GET'],req_header=[('Content-Type', 'text/html;charset=utf-8')],mode="staic"):
        # 是一个装饰器，用来创建链接
        # [path]链接名称
        # [URL_type]链接类型，默认为普通URL，可将此参数设为`RE`，链接就为一个正则表达式
        # [method]支持方法，默认只支持GET
        # [req_header]请求头，默认为Content-Type值为text/html;charset=utf-8
        # [mode]网页模式，默认为staic，如果为websocket，将自动创建一个webscoket，这个Websocket只有用户自己能访问
    def run(self):
        # 无参数，用来启动Dakada项目
    def seterr(self,fuc):
        # 一个装饰器，用来设置错误（指请求码为4**或5**时）处理函数
        # [fuc]不是参数，指错误处理函数
    def register_blueprint(self,blueprint):
        # 为app注册蓝图
        # [blueprint]一般指blueprint.py里的blueprint
    # 数据库操作
    #（注：以json（或字典）的第一个键为搜寻标准）
    # from dakada.Dakada import db
    class db:
        def __init__(self,link=".",cookie=False):
            # 创建数据库请求对象
            # [link]项目根目录，默认值为当前目录
            # [cookie]系统参数，不要填写
        def adddangerstr(self,dangerlist):
            # 添加危险字符（比如"\n"）
            # [dangerlist]危险字符列表
        def add(self,dblink,jsonordict_list):
            # 添加数据（操作的数据中若有危险字符将不会添加，返回"Bad data!"
            # [dblink]db文件夹下数据库文件名
            # [jsonordict_list]json（或字典）列表
        def load(self,dblink,key):
            # 加载数据，返回所有关于该键的json（或字典）值
            # [dblink]db文件夹下数据库文件名
            # [key]要搜寻的键
        def save(self,dblink,key,value):
            # 更改所有键为key的json（或字典）的值为value
            # [dblink]db文件夹下数据库文件名
            # [key]键
            # [value]值
        def delete(self,dblink,key):
            # 删除所有键为key的json（或字典）
            # [dblink]db文件夹下数据库文件名
            # [key]键
        def clear(self,dblink):
            # 清除指定数据库内容
            # [dblink]db文件夹下数据库文件名
    # websocket
    # 实际上，这里的websocket指前端javascript对websocket链接请求，python在后端处理请求后返回数据
    def newwebsocket(self，fuc):
        # 一个装饰器，用于设置websocket处理函数
        # [fuc]不是参数，指websocket处理函数
# 模板渲染
# from dakada.render import *
def render_html(link,**kwargs):
    # 渲染模板
    # [link]要渲染的模板链接
    # [**kwargs]指Jinja2的render函数中的**kwargs
def addfilter(name):
    # 一个装饰器，用于添加过滤器
    # [name]过滤器名称
# User工具
# from dakada.User import *
def register(username,passwd,p_link=".",**another):
    # 注册用户
    # [username]用户名
    # [password]密码
    # [p_link]项目根目录，默认值为当前目录
    # [**another]注册用户的其他信息，比如用户邮箱，电话号码等
def login(ip,username,passwd,time,p_link=".",**another):
    # 登录，登陆成功将会为登录ip创建一个键为user值为登录用户名的cookie
    # [ip]登录ip
    # [username]用户名
    # [password]密码
    # [time]用户登陆时长，为一个datetime.timedelta对象
    # [p_link]项目根目录，默认值为当前目录
    # [**another]注册用户的其他信息，比如用户邮箱，电话号码等
def logout(ip,p_link="."):
    # 登出
    # [ip]登录ip
    # [p_link]项目根目录，默认值为当前目录

# Cookie
# from dakada import cookie
# （过期cookie系统自动删除）
class cookie:
     def __init__(self,p_link="."):
        # 创建cookie处理对象
        # [p_link]项目根目录，默认值为当前目录
     def add_cookies(self,ip,key,value,TTL):
        # 为ip新建cookie
        # [ip]用户ip
        # [key]cookie的键
        # [value]cookie的值
     def load_cookies(self,ip):
        # 加载指定ip的所有cookie，返回一个列表
        # [ip]用户ip
     def delete_cookies(self,ip):
        # 删除指定ip的cookie
        # [ip]用户ip
# 制作后台
# from dakada.admin import make_admin
def make_admin(HTML=True,link="."):
    # 生成管理员后台
    # [HTML]返回格式，如果为True则返回HTML代码，False则返回数据库内容，让用户自定义HTML代码
    # [link]项目根目录，默认值为当前目录
~~~
~~~
//Javascript(HTML) API
send(sendmsg,function (staus,recvmsg){
     //Your code is here...
     //当网页模式为websocket时Dakada将创建该函数
     //后端出错会返回一个键为err的消息
     //[sendmsg]要发送的消息
     //[status]状态码
     //[recvmsg]接收到的消息
})
~~~
~~~
# Dakada app实际应用

from dakada import Dakada,cookie
from dakada.render import render_html,addfilter
from dakada.admin import make_admin
from dakada.User import *
import datetime  # 需要的库
app=Dakada() # 创建一个Dakada app
# 也可以先导入使用蓝图的文件：import example
# 再导入蓝图：from dakada.blueprint import blueprint
# 最后注册blueprint：app.register_blueprint(blueprint)
@app.addpath("/")  # @blueprint.addpath("/")
def webapp(d):
    # [d]一个字典，包含许多信息
    # [d['method']]请求方法
    # [d["req_ip"]]请求ip
    # [d["req_json"]]请求json，如果没有则返回None
    # [d["QUERY_STRING"]]如果用户输入的链接为/?111=2，那么将为111=2
    return "<p>hello</p>"  # response
@app.seterr
def error(e):
   # [e]错误状态码（4**，5**）
   return e
@app.addpath("/testweb",mode="websocket")  # 新建一个含有websocket的网页
def hello(d):
    return """<h1>websocket</h1><script>send("hello",function (msg){console.log(msg)});</script>"""
@app.newwebsocket
def web(msg):
    # [msg]前端发送的消息
    return {"testweb":"111"}  # 必须是一个json

~~~
