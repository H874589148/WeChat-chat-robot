# -*- coding=utf-8 -*-
import requests
import itchat
import random

KEY = '78d4424b2d2040898c521f3ba36b58d3'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        info = r.get('text')
        print("robot reply:%s" % info)
        return info
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    print(msg.User['NickName'] +":"+ msg['Text'])
    defaultReply = 'I received: ' + msg['Text']
    #robots=['——By机器人图灵','——By机器人Hawkeye','——By反正不是本人']
    reply = get_response(msg['Text'])#+random.choice(robots)
    #print (reply+"\n")
    return reply or defaultReply

@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)    #群消息的处理
def print_content(msg):
    if msg.User["NickName"]=='三人行'or msg.User["NickName"]=='另外一个你希望自动回复群的名字':    #这里可以在后面加更多的or msg.User["NickName"]=='你希望自动回复群的名字'
        print(msg.User['NickName'] +":"+ msg['Text'])     #打印哪个群给你发了什么消息
        print(get_response(msg['Text'])+"\n")           #打印机器人回复的消息
        return get_response(msg['Text'])
    else:                                         #其他群聊直接忽略
        pass

#itchat.auto_login(enableCmdQR=True)
itchat.auto_login(hotReload=True)
itchat.run()