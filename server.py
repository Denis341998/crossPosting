import vk_api.vk_api
import random
import requests
import vk
import json
# import vk.py
#import httplib2
#from BeautifulSoup4 import BeautifulSoup, SoupStrainer

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

import vk
from commander import Commander

global Random

def random_id():
    Random = 0
    Random += random.randint(0, 10000000)
    return Random


class Server:
    Photos = ['']
    Audios = ['']
    Docs = ['']

    def __init__(self, api_token, group_id, server_name: str="Empty"):

        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

        # Словарь для каждого отдельного пользователя
        self.users = {}
        self.id_user = -1
    
        # Токен
        self.tok = ''
        self.isTok = False
     
        # Группа
        self.id_group = -1

        # v
        self.v = '5.103'

    def send_msg(self, send_id, message, keyboard):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :return: None
        """
        self.vk_api.messages.send(peer_id=send_id, message=message, random_id=random_id(), keyboard=keyboard)


    def test(self):
        # Посылаем сообщение пользователю с указанным ID
        self.send_msg(158766653, "Привет-привет!")

    def start(self):
        for event in self.long_poll.listen():   # Слушаем сервер
           #print(event)

            if event.object.from_id not in self.users:
                self.users[event.object.from_id] = Commander()

        # Пришло новое сообщение
            if event.type == VkBotEventType.MESSAGE_NEW:

                username = self.get_user_name(event.object.from_id)
                self.id_user = event.object.from_id
                peer_id = event.object.peer_id
                message = f"{username}, я получил ваше сообщение!"
                print("Username: " + username)
                print("Text: " + event.object.text)
                attachments = event.object.attachments

                for attachment in attachments:
                    if(attachment['type'] == 'photo'):
                        print("Photo's URL: " + self.get_photo_url(attachment['photo']))
                    if(attachment['type'] == 'audio'):
                        print("Audio's URL: " + self.get_audio_url(attachment['audio']))
                    if(attachment['type'] == 'doc'):
                        print("Doc's URL: " + self.get_doc_url(attachment['doc']))
                print("Type: ", end="")
                if event.object.id > 0:
                    print("private message")
                else:
                    print("group message")
                print(" --- ")


                if(event.object.text == "пост в вконтакте"):
                    if(self.isTok == False):
                        message = f"{username}, пройди по ссылке и нажми \"принять\" \n https://oauth.vk.com/authorize?client_id=7214092&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall%2Cgroups%2Cfriends%2Cphotos&response_type=token&v=5.103"
                        keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/none.json", "r", encoding="UTF-8").read()
                        self.send_msg(peer_id, message, keyboard)
                        message = f"{username}, отправь токен из адресной строки."
                        self.send_msg(peer_id, message, keyboard)

                    else:
                        print('tok is ok')
                        message = f"{username}, выбери, куда ты хочешь сделать пост."
                        keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/posting_place.json", "r", encoding="UTF-8").read()
                        self.send_msg(peer_id, message, keyboard)

                    #http = httplib2.Http()
                    #status, response = http.request('https://oauth.vk.com/authorize?client_id=7156870&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall%2Cgroups%2Cfriends%2Cphotos&response_type=token&v=5.103')

                    #for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
                    #    if link.has_attr('href'):
                    #        print(link['href'])
                    #tok = requests.get("https://oauth.vk.com/authorize?client_id=7156870&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall%2Cgroups%2Cfriends%2Cphotos&response_type=token&v=5.103")['response']['access_token']
                    #print(tok)

                elif(event.object.text == "пост в фейсбук"):
                    keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/posting_place.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)

                elif (event.object.text == "привет" or event.object.text == "ghbdtn"):
                    keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
                    print(self.id_user)


                elif (event.object.text == "пост на стену"):
                    r = self.make_post_to_user(self.id_user)
                    print(r)
                    message = f"{r}"
                    keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, message, keyboard)


                elif(event.object.text == "пост в группу"):
                    keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/none.json", "r", encoding="UTF-8").read()
                    message = f"{username}, выбери группы, в которые хочешь разместить пост: перечисли цифры нужных сообществ из списка через пробел.\nПример: пост 1"
                    self.send_msg(peer_id, message, keyboard)

                    grs = self.take_groups()
                    print(grs[0], grs[1], grs[2])
                    self.send_msg(peer_id, grs[2], keyboard)


                elif(event.object.text == "показать последние"):
                    keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/none.json", "r", encoding="UTF-8").read()
                    message = f"{username}, выбери группы, в которых хочешь увидеть последние посты: перечисли цифры нужных сообществ из списка через пробел.\nПример: посл 1"
                    self.send_msg(peer_id, message, keyboard)

                    grs = self.take_groups()
                    print(grs[0], grs[1], grs[2])
                    self.send_msg(peer_id, grs[2], keyboard)


                elif(event.object.text[3] == "л"):          # последние
                    num = int(event.object.text[5:]) - 1
                    print(num)
                    grs = self.take_groups()
                    id_gr = grs[1][num]

                    data = self.take_posts(id_gr, 1)
                    print(data)
                    message = f"{data}"
                    keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, message, keyboard)


                elif (event.object.text[3] == "т"):  # сделать пост
                    num = int(event.object.text[5:]) - 1
                    print(num)
                    grs = self.take_groups()
                    id_gr = grs[1][num]

                    # r = self.make_post_with_photo(id_gr, 'C:/Users/User/Desktop/Vicky/MKP/bot_new/1.jpg')
                    r = self.make_post(id_gr)
                    print(r)
                    message = f"{r}"
                    keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, message, keyboard)


                else:
                    self.tok = event.object.text
                    self.isTok = True
                    keyboard = open("C:/Users/User/Desktop/Vicky/MKP/bot_new/keyboards/posting_place.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)




    def get_user_name(self, user_id):
        """ Получаем имя пользователя"""
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']

    # def get_user_groups(self, user_id):
    #     """ Получаем группы пользователя"""
    #     return self.vk_api.groups.get(user_id=user_id)

    def get_photo_url(self, photo):
        """ Получаем прикрепленное фото"""
        ph = photo['sizes'][6]['url']
        # ids = 900195
        # mes = requests.get("https://api.vk.com/method/messages.getById", params={
        #                                                                          'message_ids': ids,
        #                                                                          'extended': 1,
        #                                                                          'group_id': self.id_group
        #                                                                         }).json()
        #
        # ph = mes['response']['items']['attachments']['photo']['id']

        self.Photos.append(ph)
        return ph

    def get_audio_url(self, audio):
        """ Получаем прикрепленное аудио"""
        au = audio['url']
        self.Audios.append(au)
        #print(self.Audios)
        return au

    def get_doc_url(self, doc):
        """ Получаем прикрепленный документ"""
        dc = doc['url']
        self.Docs.append(dc)
        return dc


# ***************************************************************************

    def savePhotoToServ(self, id_gr, str):

        # str - 'V://I//1.jpg'  /  '1.jpg'
        s1 = requests.get("https://api.vk.com/method/photos.getWallUploadServer", params={'access_token': self.tok,
                                                                                          'v': self.v,
                                                                                          'group_id': id_gr
                                                                                          }).json()

        upload_url = s1['response']['upload_url']

        file = {'file1': open(str, 'rb')}
        upload_resp = requests.post(upload_url, files=file).json()

        s2 = requests.get("https://api.vk.com/method/photos.saveWallPhoto", params={'access_token': self.tok,
                                                                                    'v': self.v,
                                                                                    'group_id': id_gr,
                                                                                    # upload_resp['gid']
                                                                                    'photo': upload_resp['photo'],
                                                                                    'server': upload_resp['server'],
                                                                                    'hash': upload_resp['hash']
                                                                                    }).json()

        return s2


    def make_post_with_photo(self, id_gr, *ph):

        # str's with adresses of photos

        str = ''

        for x in ph:
            s2 = self.savePhotoToServ(id_gr, x)

            owner_id = s2['response'][0]['owner_id'].__str__()
            id = s2['response'][0]['id'].__str__()

            str += 'photo' + owner_id + '_' + id + ','

        str = str[:-1]
        g = id_gr * (-1)

        data = requests.get("https://api.vk.com/method/wall.post", params={'access_token': self.tok,
                                                                           'v': self.v,
                                                                           'owner_id': g,
                                                                           'from_group': 1,
                                                                           'attachments': str,
                                                                           'message': 'TEST WALL POST photo'
                                                                           }).json()

        return data


    def make_post(self, id_gr):  # OK
        g = id_gr * (-1)
        data = requests.get("https://api.vk.com/method/wall.post", params = {'access_token': self.tok,
                                                                         'v': self.v,
                                                                         'owner_id': g,
                                                                         'from_group': 1,
                                                                         'attachments': 'photo99355143_457247901',
                                                                         'message': 'TEST BOT POST'
                                                                        }).json()
        return data


    def make_post_to_user(self, id_us):  # OK
        data = requests.get("https://api.vk.com/method/wall.post", params = {'access_token': self.tok,
                                                                         'v': self.v,
                                                                         'owner_id': id_us,
                                                                         'attachments': 'photo99355143_457247901',
                                                                         'message': 'TEST BOT POST'
                                                                        }).json()
        return data


    def take_posts(self, id_gr, cnt):
        g = id_gr * (-1)

        response = requests.get("https://api.vk.com/method/wall.get", params={'access_token': self.tok,
                                                                              'v': self.v,
                                                                              'owner_id': g,
                                                                              'count': cnt
                                                                              }).json()

        data = response['response']['items']

        return data


    def take_groups(self):  # OK
        grs = requests.get("https://api.vk.com/method/groups.get", params={'access_token': self.tok,
                                                                            'user_id': self.id_user,
                                                                            'extended': 1,
                                                                            'filter': 'admin',
                                                                            # 'fields': 'name',
                                                                            'v': self.v
                                                                            }).json()

        numbs = []
        ids = []
        names = []
        cnt = grs['response']['count']

        for i in range(cnt):
            numbs.append(i+1)
            ids.append(grs['response']['items'][i]['id'])
            names.append(grs['response']['items'][i]['name'])

        data = [numbs, ids, names]

        return data
