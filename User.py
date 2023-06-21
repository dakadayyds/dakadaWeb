from dakada.Dakada import db
from dakada import cookie
def getobj(p_link):
    global database
    global c_h
    try:
        database
        c_h
    except:
        database=db(p_link)
        c_h=cookie(p_link)
    finally:
        return (database,c_h)
def create_user_table(p_link):
    with open(p_link+"\\db\\User.json","a+",encoding="UTF-8") as f:
        pass
def register(username,passwd,p_link=".",**another):
    create_user_table(p_link)
    database,c_h=getobj(p_link)
    if database.add("User.json",[{"user":username,"passwd":passwd,"any":another}])=="Bad data!":
        return "failed"
def login(ip,username,passwd,time,p_link=".",**another):
    create_user_table(p_link)
    database,c_h=getobj(p_link)
    mylist=database.load("User.json","user")
    if mylist==[]:
        return False
    else:
        for my in mylist:
            if str(my)==str(dict(user=username,passwd=passwd,any=another)):
                c_h.add_cookies(ip,"user",username,time)
                return True
            else:
                continue
        return False
def logout(ip,p_link="."):
    database,c_h=getobj(p_link)
    c_h.delete_cookies(ip)
