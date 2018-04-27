# -*- coding: utf-8 -*-
import vk_api

def getMessage(val, vk):
    vk.method('messages.get',val)

def sendMessage(user_id, s, vk):
    vk.method('messages.send',{'user_id':user_id,'messages':s})

def main():
    login, password = '89528077892', 'asd456asd'
    vk_session = vk_api.VkApi(login, password)

    val = {'out':0,'count':100,'time_offset':60}

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

   # response = vk.wall.get(count=1)  # Используем метод wall.get
#user_id': 478199888 - шутка минутка
#user_id': 17093571 - дрон
#
#
#
    res = vk.messages.getDialogs()
    if res['items']:
        for x in range(res['count']):
            print(res['items'][x])
            print('\r\n')
            print(res['items'][x][u'message'])
            print('\r\n')
            print(res['items'][x][u'message'][u'user_id'])
            print('\r\n')
            print(res['items'][x][u'message'][u'title'])
            print('\r\n=======================================================\r\n')

if __name__ == '__main__':
    main()