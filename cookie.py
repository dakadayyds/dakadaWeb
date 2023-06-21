from dakada.Dakada import db
import datetime
class cookie:
    def __init__(self,p_link="."):
        self.link=p_link+"\\"
        self.cookiehandler=db(self.link,True)
    def add_cookies(self,ip,key,value,TTL):
        self.cookiehandler.add("cookies.txt",[{ip:{key:value},"time_to_live":datetime.datetime.now()+TTL}])
    def load_cookies(self,ip):
        return self.cookiehandler.load("cookies.txt",ip)
    def delete_cookies(self,ip):
        self.cookiehandler.delete("cookies.txt",ip)
import sys
sys.modules[__name__]=cookie