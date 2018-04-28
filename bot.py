# -*- coding: utf-8 -*-
import vk_api

def main():
    login, password = '89528077892', 'asd456asd'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

    print('start\r\n')

    while True:
        res = vk.messages.getDialogs(unread=1)
        if res['items']:
            for x in range(res['count']):
                if u'chat_id' in res['items'][x][u'message']:
                    currentID=res['items'][x][u'message'][u'chat_id']+2000000000 
                else:
                    currentID=res['items'][x][u'message'][u'user_id']

                print(res['items'][x][u'message'][u'body'])
                print(res['items'][x][u'message'],'message')
                print('\r\n=======================================================\r\n')

                if u'attachments' in res['items'][x][u'message']:
                    if u'type' in res['items'][x][u'message'][u'attachments']:
                        if res['items'][x][u'message'][u'attachments'][u'type'] == u'photo':
                             vk.messages.send(peer_id=currentID, message='ЗАЗАЗАЗ смешная картинка БУгагашечка!')
                vk.messages.markAsRead(peer_id=currentID)
                             
    print('end\r\n')
if __name__ == '__main__':
    main()

#print unicode(r'\u0434\u0438\u0435\u0442\u0430', 'unicode-escape')