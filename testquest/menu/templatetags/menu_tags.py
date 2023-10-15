from django import template

from menu.models import *

register = template.Library()
actual_menu_names = []
actual_menus_items = []

@register.inclusion_tag('menu/menu_elements.html')
def draw_menu(menu_name, url):
    global actual_menu_names
    global actual_menus_items
    url = url.split("/")
    menu_opened = url[2:-1]
    if menu_name in actual_menu_names:
        items = actual_menus_items[actual_menu_names.index(menu_name)]
    else:
        actual_menu_names.append(menu_name)
        try:
            items = Item.objects.filter(menu=Menu.objects.get(title=menu_name))
            actual_menus_items.append(items)
        except Menu.DoesNotExist:
            print("Menu with this name does not exist")
        except Menu.MultipleObjectReturned:
            print("There are more than 1 menu with this name")
    tmp = []
    if len(menu_opened)>0:
        for i in items:
            if i.title == menu_opened[-1]:
                tmp.append(i)
    fl = False
    its = []
    for i in tmp:
        opened_items = []
        itemforcheck = i
        if itemforcheck.motherItem == None:
            opened_items.append(itemforcheck)
            fl = True
        else:
            while itemforcheck.motherItem.title in menu_opened:
                opened_items.append(itemforcheck)
                itemforcheck = itemforcheck.motherItem
                if itemforcheck.motherItem == None:
                    opened_items.append(itemforcheck)
                    fl = True
                    break
        if fl:
            its = pack(menu_name, items, opened_items, url[1])
    if len(menu_opened) == 0:
        its = pack(menu_name, items, [], url[1])
    return {'menu': its, 'menu_url': "/"+menu_name+"/", 'menu_name': menu_name}


def pack(menu_name, items, opened_items, url_menu):
    itemList = []
    if menu_name == url_menu:
        for i in items:
            if i.motherItem == None:
                i.level = 10
                i.url = "/"+menu_name+"/"+i.title+"/"
                itemList.append(i)
            elif i.motherItem in opened_items:
                i.level = 10+10 * (len(opened_items) - opened_items.index(i.motherItem))
                i.url = itemList[itemList.index(i.motherItem)].url+i.title+"/"
                itemList.insert(itemList.index(i.motherItem)+1, i)
    return itemList