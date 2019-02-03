import itchat
import requests

# 登录微信
# itchat.login()
itchat.auto_login(hotReload=True)
# 获取微信好友发的消息
#apiUrl = "http://openapi.tuling123.com/openapi/api/v2"
apiUrl = "http://www.tuling123.com/openapi/api"

def get_info(message):
    data={
        'key':'78d4424b2d2040898c521f3ba36b58d3',
        'info':message,
        'userid':'robot'
    }
    try:
        r = requests.post(apiUrl,data=data).json()
        info = r['text']
        print("robot reply:%s"%info)
        return info
    except:
        return

get_info("你好")
# 根据发的消息回复

# 回复给微信好友
@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    defaultReply = "我知道了"
    realFriend = itchat.search_friends(name='爸爸')
    realFriendsName = realFriend[0]['UserName']
    # 打印好友回复的信息
    print("message:%s"%msg['Text'])
    # 调用图灵接口
    reply = get_info(msg['Text'])
    if msg['FromUserName'] == realFriendsName:
        itchat.send(reply,toUserName=realFriendsName)
itchat.run()