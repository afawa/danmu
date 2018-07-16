# -*- coding: utf-8 -*-
def onQQMessage(bot, contact, member, content):
    if contact.name=='弹幕测试群':
        with open(r'C:\Users\Yiming He\Desktop\qq_chatting_danmu.txt','a') as f:
            f.write(content+'\n')
