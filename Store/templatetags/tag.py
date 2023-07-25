from django import template
from random import choice

register = template.Library()


@register.filter(name="parseRandom")
def parseRandom(model, name):
    imgs = []
    for m in model:
        if str(m) == name:
            imgs.append(m.url)
    if len(imgs) > 0:
        return choice(imgs)


# def exclude(form, names):
#     names = names.split(" ")
#     form.


@register.filter(name="parse_n")
def parse_n(model, name):
    imgs = []
    for m in model:
        if str(m) == name[:-1]:
            imgs.append(m.url)
    if len(imgs) > 0:
        return imgs[-1]
    

@register.filter(name="TypeCastTo")
def TypeCastTo(dataType, to):
    print(dataType, to, "\n"*55)
    convert = {
        "string":str,
        "integer":int
    }
    print(type(convert[to](dataType)))
    return str(dataType)