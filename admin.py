import os
from jinja2 import Template,Environment
env=Environment()
def getkey(value1):
    return ",".join(list(value1.keys()))
def getvalue(value1):
    return ",".join(list(value1.values()))
env.filters['getkey'] = getkey
env.filters['getvalue'] = getvalue
def make_admin(HTML=True,link="."):
    link+="\\db"
    list1=[]
    for json in os.listdir(link):
        with open(link+"\\"+json, "r", encoding="UTF8") as f:
            list2=f.readlines()
            list3=[]
            for json2 in list2:
                list3.append(eval(json2.split("\n")[0]))
        list1.append({"title":json.split(".")[0],"text":list3})
    if HTML:
        admin_template='''
        <!DOCTYPE html>
    {%for json in list1%}
        <h1>{{json.title}}</h1><br/>
        <style>
table{
    width: 40%;
    border-collapse: collapse;
}

table caption{
    font-size: 2em;
    font-weight: bold;
    margin: 1em 0;
}

th,td{
    border: 1px solid #999;
    text-align: center;
    padding: 20px 0;
}

table thead tr{
    background-color: #000000;
    color: #fff;
}

table tbody tr:nth-child(odd){
    background-color: #eee;
}





table tfoot tr td{
    text-align: right;
    padding-right: 20px;
}
    </style>
        <table border="1">
        <thead>
            <tr>
                <th>key</th>
                <th>value</th>
            </tr>
        </thead>
        <tbody>
            {%for every_json in json.text%}
                <tr>
                    <td>{{every_json|getkey}}</td>
                    <td>{{every_json|getvalue}}</td>
                </tr>
            {%endfor%}
        </table>
    {%endfor%}
                    '''
        return env.from_string(admin_template).render(list1=list1)
    else:
        return list1