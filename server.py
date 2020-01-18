import vk_api.vk_api
import random
import facebook
import requests
import vk
import fb
import json
import config
import re
import pymysql
import string

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
    Videos = ['']

    def __init__(self, api_token, group_id, server_name: str = "Empty"):

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

        # Токен вк
        # self.tok = '34042d3de4093a70bc56e392162cf6f1d8f6919ed39a2bc88c2a8fdf87f4eed2d79a70057fced0170ab50'
        self.tok = ''
        self.isTok = False
        # self.isTok = True

        # Токен facebook
        # self.fb_tok = 'EAAHh0PN7IvABAKLXg9yYqNEZAlxPAelhfRpKHOh5ZCNO7pajm3I0PY46X2cq0nyWAf1Eb13CAybgoOFg3Y2BpI1csk8GDQkXPhomzGjsJcp2GrHrXP2gKTkVu4ZBSQBzgkA1JF42iIMe2271RJsZBCiP49h14HSfRPtz0KMflGoKZCBMblOUjVwhkIPxvaccZD'
        self.fb_tok = ''
        self.is_fb_tok = False
        # self.is_fb_tok = True

        # Выбран fb/vk
        # self.is_fb = False
        # self.is_vk = False

        # Группа
        self.id_group = -1
        self.id_grs = []
        self.my_grs = []
        self.cnt_groups = 1

        # v
        self.v = '5.103'

        # attach
        self.attach = ""
        self.attach_fb = ""

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
        for event in self.long_poll.listen():  # Слушаем сервер

            # con = pymysql.connect('localhost', 'root', 'Alibet201234', 'crossposting')

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
                    if (attachment['type'] == 'photo'):
                        self.attach += self.get_photo_url(attachment['photo']) + ','
                        print("Photo's URL: " + self.get_photo_url(attachment['photo']))
                        self.attach_fb = self.get_photo_url2(attachment['photo'])
                        print("Photo's URL: " + self.get_photo_url2(attachment['photo']))
                    if (attachment['type'] == 'audio'):
                        self.attach += self.get_audio_url(attachment['audio']) + ','
                        print("Audio's URL: " + self.get_audio_url(attachment['audio']))
                        self.attach_fb = self.get_audio_url2(attachment['audio'])
                        print("Audio's URL: " + self.get_audio_url2(attachment['audio']))
                    if (attachment['type'] == 'doc'):
                        self.attach += self.get_doc_url(attachment['doc']) + ','
                        print("Doc's URL: " + self.get_doc_url(attachment['doc']))
                        self.attach_fb = self.get_doc_url2(attachment['doc'])
                        print("Doc's URL: " + self.get_doc_url2(attachment['doc']))
                    if (attachment['type'] == 'video'):
                        self.attach += self.get_video_url(attachment['video']) + ','
                        print("Video's URL: " + self.get_video_url(attachment['video']))
                print("Type: ", end="")
                if event.object.id > 0:
                    print("private message")
                else:
                    print("group message")
                print(" --- ")

                if (event.object.text == "привет" or event.object.text == "Привет" or event.object.text == "ghbdtn" or event.object.text == "Ghbdtn"
                        or event.object.text == "Hi" or event.object.text == "hi" or event.object.text == "Рш" or event.object.text == "рш"):
                    keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
                    print(self.id_user)


                elif (event.object.text == "пост в фейсбук"):  # ??????????????
                    if (self.is_fb_tok == False):
                        '''with con:
                            cur = con.cursor()
                            cur.execute("SELECT token FROM sites "
                                        "INNER JOIN user_site ON user_site.site_id = sites.site_id "
                                        "INNER JOIN users ON users.user_id = user_site.users_id ")
                            token = cur.fetchone()

                        if (token):
                            print(token[0])
                            self.fb_tok = token[0]
                            keyboard = open("keyboards/fb.json", "r", encoding="UTF-8").read()
                            self.send_msg(peer_id, 'С возвращением!', keyboard)
                        else:'''
                        # print(token)


                elif (event.object.text == "назад"):
                    keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
                    print(self.id_user)



                elif (event.object.text == "сделать пост"):
                    if not self.tok:
                        # '''with con:
                        #                             cur = con.cursor()
                        #                             cur.execute("SELECT token FROM sites "
                        #                                         "INNER JOIN user_site ON user_site.site_id = sites.site_id "
                        #                                         "INNER JOIN users ON users.user_id = user_site.users_id ")
                        #                             token = cur.fetchone()
                        #                             token = token[0]
                        #                         if (token):
                        #                             print(token)
                        #                             self.tok = token
                        #                             keyboard = open("keyboards/posting_place.json", "r", encoding="UTF-8").read()
                        #                             self.send_msg(peer_id, 'С возвращением!', keyboard)
                        #                         else:'''
                        # print(token)

                        message = f"{username}, пройди по ссылке и нажми \"принять\" \n https://oauth.vk.com/authorize?client_id=7173850&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall%2Cgroups%2Cfriends%2Cphotos&response_type=token&v=5.103 \n"
                        keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                        message += f"{username}, отправь токен из адресной строки (от 'access_token=' до '&expires_in').\nПример: vk \'token\'"
                        self.send_msg(peer_id, message, keyboard)


                    elif not self.fb_tok:

                        # with con:
                        #     cur = con.cursor()
                        #     cur.execute("SELECT token FROM sites "
                        #                 "INNER JOIN user_site ON user_site.site_id = sites.site_id "
                        #                 "INNER JOIN users ON users.user_id = user_site.users_id ")
                        #     token = cur.fetchone()
                        #
                        # if (token):
                        #     print(token[0])
                        #     self.fb_tok = token[0]
                        #     keyboard = open("keyboards/fb.json", "r", encoding="UTF-8").read()
                        #     self.send_msg(peer_id, 'С возвращением!', keyboard)
                        # else:
                        #     print(token)

                        message = f"{username}, пройди по ссылке регистрации в facebook\n https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=manage_pages,publish_pages&response_type=token&enable_profile_selector=1&profile_selector_ids=pageid"
                        keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                        message += f"{username}, После регистрации успей отправить нам адрес страницы.\nПример: fb \'token\'"
                        self.send_msg(peer_id, message, keyboard)

                    else:
                        keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                        message = f"{username}, выбери группы, в которые хочешь разместить пост: перечисли цифры нужных сообществ из списка через пробел.\nПример: \"пост 1 2\" или \"post 1\""
                        self.send_msg(peer_id, message, keyboard)

                        grs = self.take_groups_vk_fb()
                        print(grs[0], grs[1], grs[2], grs[3])  # grs[4]
                        self.send_msg(peer_id, grs[3], keyboard)

                elif (event.object.text == "показать последние"):
                    if not self.tok:
                        '''with con:
                                                    cur = con.cursor()
                                                    cur.execute("SELECT token FROM sites "
                                                                "INNER JOIN user_site ON user_site.site_id = sites.site_id "
                                                                "INNER JOIN users ON users.user_id = user_site.users_id ")
                                                    token = cur.fetchone()
                                                    token = token[0]
                                                if (token):
                                                    print(token)
                                                    self.tok = token
                                                    keyboard = open("keyboards/posting_place.json", "r", encoding="UTF-8").read()
                                                    self.send_msg(peer_id, 'С возвращением!', keyboard)
                                                else:'''

                        message = f"{username}, пройди по ссылке и нажми \"принять\" \n https://oauth.vk.com/authorize?client_id=7173850&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall%2Cgroups%2Cfriends%2Cphotos&response_type=token&v=5.103 \n"
                        keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                        message += f"{username}, отправь токен из адресной строки (от 'access_token=' до '&expires_in').\nПример: vk \'token\'"
                        self.send_msg(peer_id, message, keyboard)

                    elif not self.fb_tok:

                        message = f"{username}, пройди по ссылке регистрации в facebook\n https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=manage_pages,publish_pages&response_type=token&enable_profile_selector=1&profile_selector_ids=pageid"
                        keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                        message += f"{username}, После регистрации успей отправить нам адрес страницы.\nПример: fb \'token\'"
                        self.send_msg(peer_id, message, keyboard)


                    else:
                        keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                        message = f"{username}, выбери группы, в которых хочешь увидеть последние посты: перечисли цифры нужных сообществ из списка через пробел.\nПример: \"посл 1\" или \"last 1\"\nЕсли хочешь увидеть самый последний опубликованый пост, отправь \"last 0\" или \"посл 0\""
                        self.send_msg(peer_id, message, keyboard)

                        grs = self.take_groups_vk_fb()
                        print(grs[0], grs[1], grs[2], grs[3])
                        self.send_msg(peer_id, grs[3], keyboard)


                elif (len(event.object.text) >= 6 and (re.match(r'last', event.object.text) or re.match(r'посл', event.object.text))):  # последние
                    num = int(event.object.text[5:]) - 1
                    print(num)

                    if num == -1:
                        message = f"Пока не работает"
                        keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                        self.send_msg(peer_id, message, keyboard)

                    else:
                        grs = self.take_groups_vk()
                        id_gr = grs[1][num]

                        data = self.take_posts(id_gr, 1)
                        print ("data: ")
                        print(data)
                        message = f"\"" + data[0]['text'] + "\"\n"

                        try:
                            type = data[0]['attachments'][0]['type']
                            print (type)
                            url = data[0]['attachments'][0][type]['sizes'][0]['url']
                            print (url)
                            message += url

                        except Exception:
                            print("No attachments")

                        keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                        self.send_msg(peer_id, message, keyboard)

                    self.cnt_groups = 1


                elif (len(event.object.text) >= 4 and (re.match(r'send', event.object.text) or re.match(r'отпр', event.object.text))):
                    text = ""

                    if len(event.object.text) >= 6:
                        text = event.object.text[5:]

                    # отправки постов в выбранные группы
                    cnt = len(self.my_grs)
                    r = []
                    ids = ""
                    print(self.my_grs)

                    for i in range(cnt):
                        r.append(self.make_post_vk_fb(self.my_grs[i], text, self.attach))

                        if(self.my_grs[i][3] == 'vk'):
                            ids += r[i][0]['response']['post_id'].__str__()
                            ids += ","

                    if(len(ids) > 1):
                        ids = ids[:-1]
                    print(r)

                    self.my_grs.clear()
                    self.attach = ""
                    self.cnt_groups = 1

                    message = "Посты отправлены."

                    #if (len(ids) > 1):
                    #     message += " ID постов: " + ids
                    keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, message, keyboard)


                elif (len(event.object.text) >= 6 and (re.match(r'post', event.object.text) or re.match(r'пост', event.object.text))):
                    # получение порядковых номеров выбранных групп
                    arr_num = event.object.text[5:]
                    arr_num = arr_num.split(' ')
                    cnt = len(arr_num)

                    for i in range(cnt):  # № групп
                        tmp = int(arr_num[i]) - 1
                        arr_num[i] = tmp

                    print(arr_num)

                    # получение всех групп пользователя
                    grs = self.take_groups_vk_fb()

                    # получение id выбранных групп
                    for i in range(cnt):
                        self.id_grs.append(grs[1][arr_num[i]])

                        num = grs[0][arr_num[i]]
                        id = grs[1][arr_num[i]]
                        name = grs[2][arr_num[i]]
                        # str_name = grs[3][arr_num[i]]
                        own = grs[4][arr_num[i]]
                        gr = [num, id, name, own]
                        self.my_grs.append(gr)

                    print(self.id_grs)
                    print(self.my_grs)

                    message = f"{username}, введи пост \nПример: \"отпр \'текст\'\" или \"send \'текст\'\""
                    keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, message, keyboard)


                elif re.match(r'vk [a-z0-9]{85}', event.object.text):  # and len(event.object.text) == 85: # token
                    self.tok = event.object.text[3:]
                    print(self.tok)
                    self.isTok = True
                    keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, 'Токен VK получен', keyboard)

                    if not self.fb_tok:
                        message = f"{username}, пройди по ссылке регистрации в facebook\n https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=manage_pages,publish_pages&response_type=token&enable_profile_selector=1&profile_selector_ids=pageid"
                        keyboard = open("keyboards/back.json", "r", encoding="UTF-8").read()
                        # self.send_msg(peer_id, message, keyboard)
                        message += f"{username}, После регистрации успей отправить нам адрес страницы.\nПример: fb \'token\'"
                        self.send_msg(peer_id, message, keyboard)

                    # rand = random_id()
                    # with con:
                    #     cur = con.cursor()
                    #     cur.execute("INSERT INTO sites (site_id, login, password, token, name, address) VALUES (%s, %s, %s, %s, %s, %s)", [rand, '', '', self.tok, '', ''])
                    #     cur.execute("INSERT INTO users (user_id, first_name, last_name, picture) VALUES (%s, %s, %s, %s)",
                    #         [event.object.from_id, "", "", ""])
                    #     cur.execute("INSERT INTO user_site (users_id, site_id) VALUES (%s, %s)", [event.object.from_id, rand])

                    # elif (self.is_fb == True):
                    #     self.fb_tok = event.object.text
                    #     self.fb_tok = self.get_token_from_url(self.fb_tok)
                    #     self.is_fb_tok = True
                    #     keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    #     # keyboard = open("keyboards/fb.json", "r", encoding="UTF-8").read()
                    #     # self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
                    #     self.send_msg(peer_id, 'Токен FB получен', keyboard)

                    #     rand = random_id()
                    #     with con:
                    #         cur = con.cursor()
                    #         cur.execute("INSERT INTO sites (site_id, login, password, token, name, address) VALUES (%s, %s, %s, %s, %s, %s)", [rand, '', '', self.fb_tok, '', ''])
                    #         cur.execute("INSERT INTO users (user_id, first_name, last_name, picture) VALUES (%s, %s, %s, %s)",
                    #             [event.object.from_id, "", "", ""])
                    #         cur.execute("INSERT INTO user_site (users_id, site_id) VALUES (%s, %s)", [event.object.from_id, rand])

                    # else:   # ???
                    #     keyboard = open("keyboards/none.json", "r", encoding="UTF-8").read()
                    #     #self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
                    #     self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)


                elif re.match(r'fb [a-zA-Z0-9]+', event.object.text):  # and len(event.object.text) == 85: # token
                    self.fb_tok = event.object.text[3:]
                    # self.fb_tok = self.get_token_from_url(self.fb_tok)
                    self.is_fb_tok = True
                    keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, 'Токен FB получен', keyboard)

                    if not self.tok:
                        '''with con:
                                                    cur = con.cursor()
                                                    cur.execute("SELECT token FROM sites "
                                                                "INNER JOIN user_site ON user_site.site_id = sites.site_id "
                                                                "INNER JOIN users ON users.user_id = user_site.users_id ")
                                                    token = cur.fetchone()
                                                    token = token[0]
                                                if (token):
                                                    print(token)
                                                    self.tok = token
                                                    keyboard = open("keyboards/posting_place.json", "r", encoding="UTF-8").read()
                                                    self.send_msg(peer_id, 'С возвращением!', keyboard)
                                                else:'''

                        message = f"{username}, пройди по ссылке и нажми \"принять\" \n https://oauth.vk.com/authorize?client_id=7173850&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall%2Cgroups%2Cfriends%2Cphotos&response_type=token&v=5.103 \n"
                        keyboard = open("keyboards/back.json", "r",
                                        encoding="UTF-8").read()
                        message += f"{username}, отправь токен из адресной строки (от 'access_token=' до '&expires_in').\nПример: vk \'token\'"
                        self.send_msg(peer_id, message, keyboard)

                    #     rand = random_id()
                    #     with con:
                    #         cur = con.cursor()
                    #         cur.execute("INSERT INTO sites (site_id, login, password, token, name, address) VALUES (%s, %s, %s, %s, %s, %s)", [rand, '', '', self.fb_tok, '', ''])
                    #         cur.execute("INSERT INTO users (user_id, first_name, last_name, picture) VALUES (%s, %s, %s, %s)",
                    #             [event.object.from_id, "", "", ""])
                    #         cur.execute("INSERT INTO user_site (users_id, site_id) VALUES (%s, %s)", [event.object.from_id, rand])

                else:
                    keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, 'Команда не распознана', keyboard)


    def get_user_name(self, user_id):
        """ Получаем имя пользователя"""
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']

    def get_photo_url(self, photo):
        own_id = photo['owner_id'].__str__()
        ph_id = photo['id'].__str__()
        str = "photo" + own_id + "_" + ph_id
        return str

    def get_photo_url2(self, photo):
        ph = photo['sizes'][6]['url']
        self.Photos.append(ph)
        return ph

    def get_audio_url(self, audio):
        own_id = audio['owner_id'].__str__()
        audio_id = audio['id'].__str__()
        str = "audio" + own_id + "_" + audio_id
        return str

    def get_audio_url2(self, audio):
        au = audio['url']
        self.Audios.append(au)
        # print(self.Audios)
        return au

    def get_doc_url(self, doc):
        own_id = doc['owner_id'].__str__()
        doc_id = doc['id'].__str__()
        str = "doc" + own_id + "_" + doc_id
        return str

    def get_doc_url2(self, doc):
        dc = doc['url']
        self.Docs.append(dc)
        return dc

    def get_video_url(self, video):
        own_id = video['owner_id'].__str__()
        video_id = video['id'].__str__()
        str = "video" + own_id + "_" + video_id
        return str

    # ***************************************************************************

    def take_groups_vk_fb(self):
        data = self.take_groups_vk()
        tmp = self.fb_get_groups()
        data[0] += tmp[0]
        data[1] += tmp[1]
        data[2] += tmp[2]
        data[3] += tmp[3]
        data[4] += tmp[4]

        self.cnt_groups = 1
        print(data)
        return data

    def make_post_vk_fb(self, gr, text, attach):
        r = []
        print(gr)
        if (gr[3] == 'vk'):
            r.append(self.make_post_vk(gr[1], text, attach))
        elif (gr[3] == 'fb'):
            r.append(self.fb_post_photo(self.attach_fb, text, gr[1]))

        return r

    def make_post_vk(self, id_gr, text, attach):
        if id_gr == self.id_user:
            data = self.make_post_to_user(id_gr, text, attach)

        else:
            g = id_gr * (-1)
            data = requests.get("https://api.vk.com/method/wall.post", params={'access_token': self.tok,
                                                                               'v': self.v,
                                                                               'owner_id': g,
                                                                               'from_group': 1,
                                                                               'attachments': attach,
                                                                               # 'photo99355143_457247901',
                                                                               'message': text  # 'TEST BOT POST'
                                                                               }).json()
        return data

    def savePhotoToServ(self, id_gr, str):
        return 0

    #
    #     # str - 'V://I//1.jpg'  /  '1.jpg'
    #     s1 = requests.get("https://api.vk.com/method/photos.getWallUploadServer", params={'access_token': self.tok,
    #                                                                                       'v': self.v,
    #                                                                                       'group_id': id_gr
    #                                                                                       }).json()
    #
    #     upload_url = s1['response']['upload_url']
    #
    #     file = {'file1': open(str, 'rb')}
    #     upload_resp = requests.post(upload_url, files=file).json()
    #
    #     s2 = requests.get("https://api.vk.com/method/photos.saveWallPhoto", params={'access_token': self.tok,
    #                                                                                 'v': self.v,
    #                                                                                 'group_id': id_gr,
    #                                                                                 # upload_resp['gid']
    #                                                                                 'photo': upload_resp['photo'],
    #                                                                                 'server': upload_resp['server'],
    #                                                                                 'hash': upload_resp['hash']
    #                                                                                 }).json()
    #
    #     return s2
    #
    #
    # def make_post_with_photo(self, id_gr, *ph):
    #
    #     # str's with adresses of photos
    #
    #     str = ''
    #
    #     for x in ph:
    #         s2 = self.savePhotoToServ(id_gr, x)
    #
    #         owner_id = s2['response'][0]['owner_id'].__str__()
    #         id = s2['response'][0]['id'].__str__()
    #
    #         str += 'photo' + owner_id + '_' + id + ','
    #
    #     str = str[:-1]
    #     g = id_gr * (-1)
    #
    #     data = requests.get("https://api.vk.com/method/wall.post", params={'access_token': self.tok,
    #                                                                        'v': self.v,
    #                                                                        'owner_id': g,
    #                                                                        'from_group': 1,
    #                                                                        'attachments': str,
    #                                                                        'message': 'TEST WALL POST photo'
    #                                                                        }).json()
    #
    #     return data

    def make_post_to_user(self, id_us, text, attach):
        data = requests.get("https://api.vk.com/method/wall.post", params={'access_token': self.tok,
                                                                           'v': self.v,
                                                                           'owner_id': id_us,
                                                                           'attachments': attach,
                                                                           # 'photo99355143_457247901',
                                                                           'message': text  # 'TEST BOT POST'
                                                                           }).json()
        return data

    def take_posts(self, id_gr, cnt):
        if (id_gr == self.id_user):
            response = requests.get("https://api.vk.com/method/wall.get", params={'access_token': self.tok,
                                                                                  'v': self.v,
                                                                                  'owner_id': id_gr,
                                                                                  'count': cnt
                                                                                  }).json()
        else:
            g = id_gr * (-1)

            response = requests.get("https://api.vk.com/method/wall.get", params={'access_token': self.tok,
                                                                                  'v': self.v,
                                                                                  'owner_id': g,
                                                                                  'count': cnt
                                                                                  }).json()

        data = response['response']['items']

        return data

    def take_groups_vk(self):
        print("id_user", self.id_user)
        grs = requests.get("https://api.vk.com/method/groups.get", params={'access_token': self.tok,
                                                                           'user_id': self.id_user,
                                                                           'extended': 1,
                                                                           'filter': 'admin',
                                                                           # 'fields': 'name',
                                                                           'v': self.v
                                                                           }).json()
        print(grs)

        numbs = []
        ids = []
        names = []
        own = []
        cnt = grs['response']['count']
        str_names = ""

        numbs.append(self.cnt_groups)
        ids.append(self.id_user)
        name = (self.cnt_groups).__str__() + " " + self.get_user_name(self.id_user) + " (своя стена ВК)" + "\n"
        names.append(name)
        str_names += name
        own.append('vk')
        self.cnt_groups += 1

        for i in range(cnt):
            numbs.append(i + self.cnt_groups)
            ids.append(grs['response']['items'][i]['id'])
            name = (i + self.cnt_groups).__str__() + " " + grs['response']['items'][i]['name'] + " (ВК)" + "\n"
            names.append(name)
            str_names += name
            own.append('vk')

        self.cnt_groups = cnt + 1
        # str_names = str_names[:-1]
        data = [numbs, ids, names, str_names, own]

        return data

    ################################ facebook ################################

    # Достает токен из строки URL, которую нам дал пользователь
    def get_token_from_url(self, url):
        url = re.search("(?P<url>access_token=[\w]+)", url).group("url")
        url = url.split('=')[1]
        print(url)
        return url

    # Возвраает список групп, где пользователь - админ
    def fb_get_groups(self):
        r = requests.get(
            "https://graph.facebook.com/v5.0/me?fields=groups{administrator,id,name}&access_token=" + self.fb_tok)
        print(r, "!!!!!!!!!!!!!")
        print(r.json()['groups'])
        r = r.json()['groups']['data']
        print(r)

        numbs = []
        ids = []
        names = []
        str_names = ""
        name = ""
        own = []
        ind = 0
        for i in r:
            if (i['administrator'] == True):
                print("fb_admin")
                numbs.append(ind + self.cnt_groups + 1)
                print(ids.append(i['id']))
                name = (ind + self.cnt_groups + 1).__str__() + " " + i['name'] + " (ФБ)" + "\n"
                names.append(name)
                str_names += name
                own.append('fb')
                ind = ind + 1

        str_names = str_names[:-1]
        data = [numbs, ids, names, str_names, own]
        print(data)

        return data

    '''def auth(self):
        fb_auth_redirect_url2 = "https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=manage_pages,publish_pages&response_type=token&enable_profile_selector=1&profile_selector_ids=pageid"
        fb_auth_redirect_url2 = "https://www.facebook.com/dialog/oauth?client_id="+fb_app_id+"529762531091184&redirect_uri="+fb_redirect_uri+"&scope=manage_pages,publish_pages&response_type=token&enable_profile_selector=1&profile_selector_ids=pageid"
        x1 = webbrowser.open(fb_auth_redirect_url2, new=0, autoraise=False)
        tttoken = 'EAAHh0PN7IvABAHY3tRpZCbsZA38IFx504PLiZBjGP3DeXvKd18MkhKLpnhRy4POv9LBt2WrkZBMfnG3LZCKwfZC2G48P6ktk2ciKXODpqquaTxYlmfd0EYSxu7WO83x7wGC0cbqpjnZCHeBukH1CtunTPwWxVlvOCc4NZC200aYhvAlYESwgB8UQce3ruDjeGVgZD'
        tttoken = 'EAAHh0PN7IvABAD0AbFYZAdsMZAB8RRqWIT1LrJ5iy1Yc1MZAS8h9kZCzLOizFZAmpZAOlBTZA9HU9IZADCrFuPjyin2o3LIdmvumiIdwG2qsvKA7r9hZBTvUGjmyVj3NQ0SzTwfx6orNizNndA5FEE6Vriyq2ua5PHJAGSBb6tZAnkg4zRQSRZB05jp2pfKXGW5Re8ZD'
        print(tttoken)
        l_token = requests.get(
            "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + fb_app_id + "&client_secret=" + fb_secret + "&fb_exchange_token=" + tttoken)
        print(l_token.json()['access_token'])
        print(x1)'''

    # Получает короткий токен и возвращает длинный (90 дней)
    def get_fb_long_token(self, s_token):
        l_token = requests.get(
            "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + config.fb_app_id + "&client_secret=" + config.fb_secret + "&fb_exchange_token=" + s_token)
        print("facebook long token: ", l_token.json()['access_token'])
        return l_token.json()['access_token']

    # https: // sun9 - 46.
    # userapi.com / c857132 / v857132187 / a5df0 / FHhS0TQVJ3E.jpg
    def fb_post_photo(self, photo, text, group):
        # photo = 'https://sun9-21.userapi.com/c849532/v849532916/193b25/qd2H-t58ywo.jpg'
        # token = 'EAAHh0PN7IvABAMpZBIW3VbPGsP2i4ukDP8H7SOSKR3PnLz0z0fTDxggnyodLYsUJAIp3i3FEI92xVbIES6OCB47WCxjvcUfCaCUcXbLH7GlCT9sAS78md2ShhdgjbX0iDyA7hM32M19zGKQTX0H4Lfz04YoVyDoK2IOEChwZDZD'
        ###data = [
        ###    ('url', photo),
        ###    ('caption', text),
        ###    ('access_token', self.fb_tok),
        ###]
        print("fb_post_source", group, text, photo)
        graph = facebook.GraphAPI(access_token=self.fb_tok, version="2.12")
        print(graph.put_object(group, "feed", message=text, source=photo))
        # fb = requests.post('https://graph.facebook.com/985618928451302/photos', data=data)  # IT WORKS!!!
        ###fb = requests.post('https://graph.facebook.com/'+group+'/photos', data=data)
        ###print(fb.text)

    def fb_post_video(self, video, text, group):
        graph = fb.GraphAPI(access_token=self.fb_tok, version="2.12")  # 'fb' instesd of 'facebook'
        print(graph.put_object(
            parent_object=group,
            connection_name='feed',
            message=text,
            link=video))
