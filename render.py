from jinja2 import Template,Environment
def render_html(link,**kwargs):
    global env
    link1="templates\\"+link
    f = open(link1, "r", encoding="UTF8")
    text=f.read()
    try:
        return env.from_string(text).render(**kwargs)
    except:
        return Template(text).render(**kwargs)
def addfilter(name):
    def addf(fuc):
        global env
        try:
            env
        except:
            env=Environment()
        env.filters[name] = fuc
    return addf