import vk_api.vk_api
import random
import requests
import vk
import fb
import json
import config
import re
import pymysql

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
    Videos = ['']

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

        # Токен facebook
        self.fb_tok = ''
        self.is_fb_tok = False

        # Выбран fb/vk
        self.is_fb = False
        self.is_vk = False
     
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

            con = pymysql.connect('localhost', 'root', 'Alibet201234', 'crossposting')


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
                    if(attachment['type'] == 'video'):
                        print("Video's URL: " + self.get_video_url(attachment['video']))
                print("Type: ", end="")
                if event.object.id > 0:
                    print("private message")
                else:
                    print("group message")
                print(" --- ")


                if(event.object.text == "пост в вконтакте"):
                    self.is_vk = True
                    self.is_fb = False

                    if(self.isTok == False):
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
                        else:
                            print(token)

                            message = f"{username}, пройди по ссылке и нажми \"принять\" \n https://oauth.vk.com/authorize?client_id=7214092&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall%2Cgroups%2Cfriends%2Cphotos&response_type=token&v=5.103"
                            keyboard = open("keyboards/none.json", "r", encoding="UTF-8").read()
                            self.send_msg(peer_id, message, keyboard)
                            message = f"{username}, отправь токен из адресной строки (от 'access_token=' до '&expires_in')."
                            self.send_msg(peer_id, message, keyboard)

                    else:
                        print('tok is ok')
                        message = f"{username}, выбери, куда ты хочешь сделать пост."
                        keyboard = open("keyboards/posting_place.json", "r", encoding="UTF-8").read()
                        self.send_msg(peer_id, message, keyboard)

                    #http = httplib2.Http()
                    #status, response = http.request('https://oauth.vk.com/authorize?client_id=7156870&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall%2Cgroups%2Cfriends%2Cphotos&response_type=token&v=5.103')

                    #for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
                    #    if link.has_attr('href'):
                    #        print(link['href'])
                    #tok = requests.get("https://oauth.vk.com/authorize?client_id=7156870&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall%2Cgroups%2Cfriends%2Cphotos&response_type=token&v=5.103")['response']['access_token']
                    #print(tok)

                elif(event.object.text == "пост в фейсбук"):
                    self.is_vk = False
                    self.is_fb = True
                    if(self.is_fb_tok == False):
                        with con:
                            cur = con.cursor()
                            cur.execute("SELECT token FROM sites "
                                        "INNER JOIN user_site ON user_site.site_id = sites.site_id "
                                        "INNER JOIN users ON users.user_id = user_site.users_id ")
                            token = cur.fetchone()
                            token = token[0]
                        if (token):
                            print(token)
                            self.fb_tok = token
                            keyboard = open("keyboards/posting_place.json", "r", encoding="UTF-8").read()
                            self.send_msg(peer_id, 'С возвращением!', keyboard)
                        else:
                            print(token)
                            message = f"{username}, пройди по ссылке регистрации в facebook\n https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=manage_pages,publish_pages&response_type=token&enable_profile_selector=1&profile_selector_ids=pageid"
                            keyboard = open("keyboards/none.json", "r", encoding="UTF-8").read()
                            self.send_msg(peer_id, message, keyboard)
                            message = f"{username}, После регистрации успей отправить нам адрес страницы."
                            self.send_msg(peer_id, message, keyboard)
                    else:
                        print('fb_tok is ok' )
                        keyboard = open("keyboards/posting_place.json", "r", encoding="UTF-8").read()
                        self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)

                elif (event.object.text == "привет" or event.object.text == "Привет" or event.object.text == "ghbdtn" or event.object.text == "Ghbdtn"):
                    keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
                    print(self.id_user)

                elif (event.object.text == "назад"):
                    keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
                    print(self.id_user)

                elif (event.object.text == "пост на стену"):
                    if(self.is_vk == True):
                        r = self.make_post_to_user(self.id_user)
                        print(r)
                        message = f"{r}"
                        keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                        self.send_msg(peer_id, message, keyboard)


                elif(event.object.text == "пост в группу"):
                    keyboard = open("keyboards/none.json", "r", encoding="UTF-8").read()
                    message = f"{username}, выбери группы, в которые хочешь разместить пост: перечисли цифры нужных сообществ из списка через пробел.\nПример: пост 1"
                    self.send_msg(peer_id, message, keyboard)

                    if(self.is_vk == True):
                        grs = self.take_groups()
                        print(grs[0], grs[1], grs[2], grs[3])
                        self.send_msg(peer_id, grs[3], keyboard)
                    elif(self.is_fb):
                        grs = self.fb_get_groups()
                        print(grs[0], grs[1], grs[2], grs[3])
                        self.send_msg(peer_id, grs[3], keyboard)

                elif(event.object.text == "показать последние"):

                    keyboard = open("keyboards/none.json", "r", encoding="UTF-8").read()
                    message = f"{username}, выбери группы, в которых хочешь увидеть последние посты: перечисли цифры нужных сообществ из списка через пробел.\nПример: посл 1"
                    self.send_msg(peer_id, message, keyboard)

                    if (self.is_vk == True):
                        grs = self.take_groups()
                        print(grs[0], grs[1], grs[2])
                        self.send_msg(peer_id, grs[2], keyboard)


                elif(len(event.object.text) >= 6 and event.object.text[3] == "л"):          # последние
                    num = int(event.object.text[5:]) - 1
                    print(num)
                    grs = self.take_groups()
                    id_gr = grs[1][num]

                    data = self.take_posts(id_gr, 1)
                    print(data)
                    message = f"{data}"
                    keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, message, keyboard)


                elif (len(event.object.text) >= 6 and event.object.text[3] == "т"):  # сделать пост
                    num = int(event.object.text[5:]) - 1
                    print(num)
                    if(self.is_vk):
                        grs = self.take_groups()
                        id_gr = grs[1][num]

                        # r = self.make_post_with_photo(id_gr, 'C:/Users/User/Desktop/Vicky/MKP/bot_new/1.jpg')
                        r = self.make_post(id_gr)
                        print(r)
                    elif(self.is_fb):
                        grs = self.fb_get_groups()
                        id_gr = grs[1][num]
                        r = self.fb_post_photo(config.photo_url,event.object.text,id_gr)

                    message = f"{r}"
                    keyboard = open("keyboards/default.json", "r", encoding="UTF-8").read()
                    self.send_msg(peer_id, message, keyboard)


                else:
                    if (self.is_vk == True):
                        self.tok = event.object.text
                        self.isTok = True
                        keyboard = open("keyboards/posting_place.json", "r", encoding="UTF-8").read()
                        # self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
                        self.send_msg(peer_id, 'Токен получен', keyboard)
                        rand = random_id()
                        with con:
                            cur = con.cursor()
                            cur.execute("INSERT INTO sites (site_id, login, password, token, name, address) VALUES (%s, %s, %s, %s, %s, %s)", [rand, '', '', self.tok, '', ''])
                            cur.execute("INSERT INTO users (user_id, first_name, last_name, picture) VALUES (%s, %s, %s, %s)",
                                [event.object.from_id, "", "", ""])
                            cur.execute("INSERT INTO user_site (users_id, site_id) VALUES (%s, %s)", [event.object.from_id, rand])


                    elif (self.is_fb == True):
                        self.fb_tok = event.object.text
                        self.fb_tok = self.get_token_from_url(self.fb_tok)
                        self.is_fb_tok = True
                        keyboard = open("keyboards/posting_place.json", "r", encoding="UTF-8").read()
                        # self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
                        self.send_msg(peer_id, 'Токен получен', keyboard)
                        rand = random_id()
                        with con:
                            cur = con.cursor()
                            cur.execute("INSERT INTO sites (site_id, login, password, token, name, address) VALUES (%s, %s, %s, %s, %s, %s)", [rand, '', '', self.fb_tok, '', ''])
                            cur.execute("INSERT INTO users (user_id, first_name, last_name, picture) VALUES (%s, %s, %s, %s)",
                                [event.object.from_id, "", "", ""])
                            cur.execute("INSERT INTO user_site (users_id, site_id) VALUES (%s, %s)", [event.object.from_id, rand])

                    else:
                        keyboard = open("keyboards/none.json", "r", encoding="UTF-8").read()
                        #self.send_msg(peer_id, self.users[event.object.from_id].input(event.object.text), keyboard)
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

    def get_video_url(self, video):
        """ Получаем прикрепленный документ"""
        vd = video['url']
        self.Videos.append(vd)
        return vd


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
        str_names = ""

        for i in range(cnt):
            numbs.append(i + 1)
            ids.append(grs['response']['items'][i]['id'])
            name = (i + 1).__str__() + " " + grs['response']['items'][i]['name'] + "\n"
            names.append(name)
            str_names += name

        str_names = str_names[:-1]
        data = [numbs, ids, names, str_names]

        return data

    #################### facebook
    #Достает токен из строки URL, которую нам дал пользователь
    def get_token_from_url(self, url):
        url = re.search("(?P<url>access_token=[\w]+)", url).group("url")
        url = url.split('=')[1]
        print(url)
        return url

    #Возвраает список групп, где пользователь - админ
    def fb_get_groups(self):
        r = requests.get(
            "https://graph.facebook.com/v5.0/me?fields=groups{administrator,id,name}&access_token=" + self.fb_tok)#EAAHh0PN7IvABANYp4AGZACdSGGI0OiiQC0UFA8BYvl6q0LaLZBg22aFRXlUpXTmF0rBkf5RxAZCCLqCZCEp2ZB8E0n3ZCsbH6NZAZCNAMriefcZBsNuIPkydOk8txTrhUsBTw7ZBVZAs4vGOOankNWkwOnY5hmsM7bRYr8ZD")
        print(r.json())
        # print(r.json()['groups'])
        r = r.json()['groups']['data']
        print(r)

        numbs = []
        ids = []
        names = []
        str_names = ""
        name = ""
        ind = 0
        for i in r:
            if (i['administrator'] == True):
                numbs.append(ind + 1)
                print(ids.append(i['id']))
                name = (ind + 1).__str__() + " " + i['name'] + "\n"
                names.append(name)
                str_names += name
                ind=ind+1

        str_names = str_names[:-1]
        data = [numbs, ids, names, str_names]

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

    #Получает короткий токен и возвращает длинный (90 дней)
    def get_fb_long_token(self, s_token):
        l_token = requests.get(
            "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + config.fb_app_id + "&client_secret=" + config.fb_secret + "&fb_exchange_token=" + s_token)
        print("facebook long token: ",l_token.json()['access_token'])
        return l_token.json()['access_token']

    def fb_post_photo(self, photo, text, group):
        # photo = 'https://sun9-21.userapi.com/c849532/v849532916/193b25/qd2H-t58ywo.jpg'
        #token = 'EAAHh0PN7IvABAMpZBIW3VbPGsP2i4ukDP8H7SOSKR3PnLz0z0fTDxggnyodLYsUJAIp3i3FEI92xVbIES6OCB47WCxjvcUfCaCUcXbLH7GlCT9sAS78md2ShhdgjbX0iDyA7hM32M19zGKQTX0H4Lfz04YoVyDoK2IOEChwZDZD'
        data = [
            ('url', photo),
            ('caption', text),
            ('access_token', self.fb_tok),
        ]
        # fb = requests.post('https://graph.facebook.com/985618928451302/photos', data=data)  # ITS WORK!!!
        fb = requests.post('https://graph.facebook.com/'+group+'/photos', data=data)
        print(fb.text)

    def fb_post_video(self, video, text, group):
        graph = facebook.GraphAPI(access_token=self.fb_tok, version="2.12")
        print(graph.put_object(
            parent_object=group,
            connection_name='feed',
            message=text,
            link=video))
