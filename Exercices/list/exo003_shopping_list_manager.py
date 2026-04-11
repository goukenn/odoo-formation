import os
from random import randint



def menu():
    """
    show application menu 
    """
    print('Shopping list Manager')
    for x in ["1. Add Item", 
            "2. Remove Item",
            "3. View list",
            "4. Check/Uncheck item",
            "5. Clear list",
            "6. Quit"]:
        print(x)

def showList(sentence):
    """
    show list of sentence
    """
    for x in sentence:
        c = 'x' if x['check'] else ' ' 
        print(f'[{c}] - {x['name']}')


def addItem(sentence):
    """
    add new item 
    """
    sentence.append({"name":input('new item: '), "check":False})

def checkItem(sentence, msg):
    """
    toggle check Item
    """
    i = int(input('(index) ? '))
    try:
        sentence[i]['check'] = not sentence[i]['check']
    except IndexError:
        msg = "index error" 
    return msg

def removeItem(sentence):
    """
    remove item 
    """
    # sentence.remove(int(input('item index ?')))
    index = int(input('item index ?'))
    del sentence[index]

def init():
    """
    initialize the modification 
    """
    return {'name': "sample...." + str(randint(0,100)), "check": True if randint(0,1) else False  }

sentence = [ init() for _ in range(4) ]
showList(sentence)
msg = None
while True:
    os.system('clear')
    menu()
    if not msg == None:
        print(msg) 
        msg = None
    try:
        action = int(input('command? '))
    except:
        continue
    if action == 6:
        break
    else:
        match action:
            case 1:
                addItem(sentence)
            case 2:
                removeItem(sentence)
            case 3:
                showList(sentence)
                print('press enter to continue...')
                input('')
            case 4:
                msg = checkItem(sentence, msg)
            case 5:
                sentence.clear()
            case _:
                msg = 'command not found'
