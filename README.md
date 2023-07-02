Dakada是一个由dakada制作的网页框架，WSGI基于python内部库wsgiref，它学习了flask，支持基础web开发，以及数据库（数据存放在后缀为`.json`的文件中）、后台制作、cookie、自行处理静态文件、蓝图（类似Flask的Blueprint）等功能，有自己的纠错功能，模板上引擎基于Jinja2，可自制过滤器，还支持用户注册、登录、登出以及webscoket等扩展功能


***

# 快速开始


首先，下载Dakada(pip install Dakada)


然后，在你的Dakada项目根目录下，运行指令`python -m dakada.startproject`


可在你的项目根目录下看到这几个文件：


![](https://asset.gitblock.cn/Media?name=FB830EFE340F1BE996848E4E960CECCF.png)


`db`:数据库文件存储地


`staic`:静态文件存储地，Dakada会自动处理他们，比如你在staic里面放入一个叫`1.js`的文件，启动项目后，访问该文件链接为`/1.js`


`templates`:模板存储地


`Blueprint.py`:项目蓝图，可通过`from blueprint import blueprint`导入该文件所存储的蓝图


`cookies.txt`:存储所有用户的cookies，使所有cookies有了一定的安全性


`debug.txt`:报错日志

`webapp.py`:主程序
