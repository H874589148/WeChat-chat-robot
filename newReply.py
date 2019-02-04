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
    print("message:%s" % msg['Text'])
    defaultReply = 'I received: ' + msg['Text']
    #robots=['——By机器人图灵','——By机器人Hawkeye','——By反正不是本人']
    reply = get_response(msg['Text'])#+random.choice(robots)
    return reply or defaultReply

#itchat.auto_login(enableCmdQR=True)
itchat.auto_login(hotReload=True)
itchat.run()