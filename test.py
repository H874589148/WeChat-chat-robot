# -*- coding=utf-8 -*-
import requests
import itchat
import random
KEY = 'ce697b3fc8b54d5f88c2fa59772cb2cf'
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
    reply = get_response(msg['Text'])
    return reply or defaultReply
itchat.auto_login(hotReload=True)
itchat.run()