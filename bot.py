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

    response = vk.wall.get(count=1)  # Используем метод wall.get

    if response['items']:
        print(response['items'][0])

if __name__ == '__main__':
    main()