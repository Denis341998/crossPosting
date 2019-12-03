import json
import urllib.request
import time
import requests
import socket
import multipart
from requests_toolbelt.multipart.encoder import MultipartEncoder
import vk_api
import random
import time
import facebook
import os
import sys
import io
import webbrowser

#### ЮРЛ для авторизации https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://vk.me/public187864217 #########
fb_auth_redirect_url = "https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://vk.me/public187864217&scope=pages_show_list,publish_to_groups,user_posts,manage_pages,publish_pages"
fb_auth_redirect_url = "https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://vk.me/public187864217&scope=manage_pages"
fb_secret='eaeb788f99bfc49e6eebac9b30d2143f'
fb_app_id='529762531091184'
fb_access_token = 'EAAHh0PN7IvABALXsqkDN6pIjjwrbm7P6lAMmUW5ZByFfD62QzXpldhHo0BtHtdxAHv7lfOAbcfwf0BqGirEb7qcznD9ii0aF3nSZBVqWuHgE2WHUmXujRuG8hWLC54GznYETj77v3HZCz1mZALyK9ZC6dHDNGpJb6tY8XY1oguwj7N3QzpDQk'
fb_viki_group_id= 'https://www.facebook.com/groups/1431304253689661'
vk_token = "a058d4a6fd9d13a115ec0a5040fed7d1cd3722a5904f2f45ceac1371a79e095265e2dde9a4c7959e26de8"
redirect_uri = 'http://api.vk.com/blank.html'
v = 5.103
id_group = -181777010
id_user = 104166508
app_id = '7173850'
video_url='https://ok.ru/video/7060785738'#'https://www.youtube.com/watch?v=l7f9yp4Sen8'#удивленный котейка
#video_url='https://youtu.be/l7f9yp4Sen8'
photo_url='https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200'#тоже котейка
photo_url2='https://s1.1zoom.ru/big3/136/Cats_Eyes_Snout_562825_3200x1800.jpg'#котейка
photo_vk_dialig_url = 'https://sun9-9.userapi.com/c857720/v857720233/eeff2/OvNXNp6JhJM.jpg'
audio_url='https://vk.com/artist/6361804539734763213'#нежность на бумаге
client_secret = 'xPHCklrdADtJ20mJC55I'
'''sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)'''



def vk_posting():
    print('VK is pressed')
    # req = "https://api.vk.com/method/wall.post?access_token=  &v=5.103&domain=prin66"

    response = requests.get("https://api.vk.com/method/wall.post", params={'access_token': vk_token,
                                                                           'v': v,
                                                                           'owner_id': id_group,
                                                                           'from_group': 1,
                                                                           'message': 'TEST WALL POST',
                                                                           'attachments': 'photo-181777010_456239047'
                                                                           })

    data = response.json()

    return data
    '''vk = vk_api.VkApi(token=vk_token)
    vk._auth_token()

    while True:
        try:
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
            if messages["count"] > 0:
                id = messages["items"][0]["last_message"]["from_id"]
                body = messages["items"][0]["last_message"]["text"]
                if body.lower() == "hi":
                    vk.method("messages.send",
                              {"peer_id": id, "message": "Hi!", "random_id": random.randint(1, 100000)})
                elif body.lower() == "by":
                    vk.method("messages.send",
                              {"peer_id": id, "message": "By!", "random_id": random.randint(1, 100000)})
                else:
                    vk.method("messages.send",
                              {"peer_id": id, "message": "Sorry?", "random_id": random.randint(1, 100000)})

        except Exception as E:
            time.sleep(1)'''

def facebook_posting():
    print('facebook is pressed')
    # получаю список фото строкой, является прямой ссылкой типа http://image.jpg
    # можно так же открывать файлы привычным способом f = open('file_path', 'rb')


    #files = 'https://vk.com/photo104166508_457240109'
    '''files = 'https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200'
    #token = access_token  # (токен пользователя)

    # передаем функции photo_id список файлов и наш токен
    media = photo_id(files, fb_access_token)
    print(media)
    # post on fb
    url = 'https://graph.facebook.com/me/feed?'
    #url = 'https://www.facebook.com/groups/985618928451302/feed?'
    data = {
        'access_token': fb_access_token###user.fb_token,
        # так же можем добавлять дополнительно links, video, files и т.д.
    }
    print(data)
    i = 0
    for id in media:
        # проходимся по нашему списку и формируем словарь
        data.update({'attached_media[%d]' % (i): '{"media_fbid": "%s"}' % (id)})
        i += 1
        print(data)
    #resp = requests.post(url, data=data)
    resp = requests.post(url, params={
        'access_token': fb_access_token,
        'owner_id': 985618928451302,
        'from_group': 1,
        'message': 'TEST WALL POST',
        'attachments': 'photo' + '985618928451302' + '_457240109'
    })'''
    graph = facebook.GraphAPI(access_token=fb_access_token)
    print(graph)
    # to post to your wall
    #photo = open('/Homiak/Documents/MDKP/Litovkin/vk_bot/Exxx4vQRmnI.jpg', 'rb')
    ###graph.put_object(985618928451302, "feed", message="тест", picture='https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200', link='https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200') #так выкладываем объект, в нашем случае текст
    #############################################
    '''access_token = fb_access_token#'ваш токен'

    data = [
        #('url', 'https://www.facebook.com/images/fb_icon_325x325.png'),  # url вашей фотографии
        #('url', 'https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200'),  # url вашей фотографии
        ('caption', 'Test text'),  # любой ваш текст который хотите публиковать
        ('access_token', access_token),  # ну и токен куда мы без него
    ]

    #fb = requests.post('https://graph.facebook.com/me/photos', data=data)
    #fb = requests.post('https://www.facebook.com/groups/985618928451302/feed', data=data)
    fb = requests.post('https://graph.facebook.com/me/feed', data=data)
    print(fb.text)'''
    ########################################
    #graph.put_object(985618928451302, "feed", message="тест", attachments='photo'+photo_url) #так выкладываем объект, в нашем случае текст
    #graph.put_object(985618928451302, "feed", message="тест", source=photo_url) #так выкладываем объект, в нашем случае текст
    #graph.put_object(985618928451302, "feed", message="тест", source=photo.read()) #так выкладываем объект, в нашем случае текст
    #photo.close()
    # to get your posts/feed
    feed = graph.get_connections("me", "feed")
    post = feed["data"]
    print(post)

# в результате получаем список id с успешно загруженными фотками
def photo_id(files, token):
    images = files.split(',')
    print(images)
    media = []
    for img in images:
        #url = 'https://graph.facebook.com/me/photos?published=false'
        url = 'https://graph.facebook.com/groups/985618928451302/photos'
        data = dict(access_token=token, caption='Test text')#, url=img)
        print(data)
        resp = requests.post(url, data)
        print(resp)
        res = json.loads(resp.text)
        print(res)
        media.append(res)
        print(media)
    return media

def fb_post_photo(url, text, token):
    #photo = 'https://sun9-21.userapi.com/c849532/v849532916/193b25/qd2H-t58ywo.jpg'  # photo_url  # photo_vk_dialig_url
    #print(token)
    token = 'EAAHh0PN7IvABAMpZBIW3VbPGsP2i4ukDP8H7SOSKR3PnLz0z0fTDxggnyodLYsUJAIp3i3FEI92xVbIES6OCB47WCxjvcUfCaCUcXbLH7GlCT9sAS78md2ShhdgjbX0iDyA7hM32M19zGKQTX0H4Lfz04YoVyDoK2IOEChwZDZD'
    data = [
        ('url', url),  # url вашей фотографии
        ('caption', text),  # любой ваш текст который хотите публиковать
        ('access_token', token),  # ну и токен куда мы без него
    ]
    #fb = requests.post('https://graph.facebook.com/985618928451302/photos', data=data)  # ITS WORK!!!
    fb = requests.post('https://graph.facebook.com/me/feed', data=data)  # ITS WORK!!!
    print(fb.text)

def tmp_func():
    # files = 'https://vk.com/photo104166508_457240109'
    '''files = 'https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200'
    #token = access_token  # (токен пользователя)

    # передаем функции photo_id список файлов и наш токен
    media = photo_id(files, fb_access_token)
    print(media)
    # post on fb
    url = 'https://graph.facebook.com/me/feed?'
    #url = 'https://www.facebook.com/groups/985618928451302/feed?'
    data = {
        'access_token': fb_access_token###user.fb_token,
        # так же можем добавлять дополнительно links, video, files и т.д.
    }
    print(data)
    i = 0
    for id in media:
        # проходимся по нашему списку и формируем словарь
        data.update({'attached_media[%d]' % (i): '{"media_fbid": "%s"}' % (id)})
        i += 1
        print(data)
    #resp = requests.post(url, data=data)
    resp = requests.post(url, params={
        'access_token': fb_access_token,
        'owner_id': 985618928451302,
        'from_group': 1,
        'message': 'TEST WALL POST',
        'attachments': 'photo' + '985618928451302' + '_457240109'
    })'''
    graph = facebook.GraphAPI(access_token=fb_access_token)
    print(graph)
    # to post to your wall
    # photo = open('/Homiak/Documents/MDKP/Litovkin/vk_bot/Exxx4vQRmnI.jpg', 'rb')
    ###graph.put_object(985618928451302, "feed", message="тест", picture='https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200', link='https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200') #так выкладываем объект, в нашем случае текст
    ############################################# Рабочая версия !!!
    access_token = fb_access_token#'ваш токен'
    #access_token = access_token.join([fb_app_id,fb_secret])
    #photo = []
    #photo.append(photo_url)
    #photo.append(photo_url2)
    #photo = ', '.join([photo_url,photo_url2])
    photo = photo_url2#photo_vk_dialig_url
    print(access_token)
    data = [
        #('url', 'https://www.facebook.com/images/fb_icon_325x325.png'),  # url вашей фотографии
        #('url', 'https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200'),  # url вашей фотографии
        ('url', photo),  # url вашей фотографии
        ('caption', 'Test text'),  # любой ваш текст который хотите публиковать
        ('access_token', access_token), # ну и токен куда мы без него
        #('content-type', 'video/mp4')
    ]

    video_url='https://vk.com/video-57876954_456253566'
    #payload = {'name': 'Name video','description': 'Opisanie', 'file_url': video_url}
    payload = [
        # ('url', 'https://www.facebook.com/images/fb_icon_325x325.png'),  # url вашей фотографии
        # ('url', 'https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200'),  # url вашей фотографии
        ('source', video_url),  # url вашей фотографии
        ('title', 'Test text'),  # любой ваш текст который хотите публиковать
        ('description', 'Test description'),  # любой ваш текст который хотите публиковать
        ('access_token', access_token),  # ну и токен куда мы без него
        #('Content-Type', 'video/mp4')
    ]
    m = MultipartEncoder(
        fields=dict(
            access_token=access_token,
            upload_phase='transfer',
            start_offset='0',#kwargs.get('start_offset'),
            upload_session_id='1363041',#kwargs.get('upload_session_id'),
            video_file_chunk=(video_url,
                              'multipart-form/data'),
        )
    )

    #m = MultipartEncoder(
    #    fields={#'field0': 'value', 'field1': 'value',
    #        ('source', video_url),  # url вашей фотографии
    #        ('title', 'Test text'),  # любой ваш текст который хотите публиковать
    #        ('description', 'Test description'),  # любой ваш текст который хотите публиковать
    #        ('access_token', fb_access_token)
    #    }
    #)

    #m = MultipartEncoder(payload)

    #url = '%s%s/videos' % (self.api_video, user.fb_user_id)
    headers = {'Content-Type': 'video/mp4'}
    #req = requests.post(url=url, data=m, headers={'Content-Type': m.content_type})
    print(data)
    print(m)

    #fb = requests.post('https://graph.facebook.com/me/photos', data=data) https://www.facebook.com/groups/1431304253689661/
    #fb = requests.post('https://www.facebook.com/groups/985618928451302/feed', data=data)
    #fb = requests.post('https://graph.facebook.com/me/feed', data=data)
    #fb = requests.post('https://graph-video.facebook.com/985618928451302/videos?access_token='+fb_access_token, data=payload)
    #fb = requests.post(url='https://graph.facebook.com/985618928451302/videos', data =payload, headers={'Content-Type': 'multipart/form-data'} )
    #class ="page_doc_title" href="/doc104166508_525827262?hash=70a2db0e93e2a32bdd&amp;dl=1870c75cab5d8fbb13" target="_blank" > Статья.docx < / a >
    href = "https://www.facebook.com/download/428108827770823/test_parser.txt?av=100041816445446&amp;eav=Afa_ZtO0agX6HzZ_5UHwyuo9qZ5WLmS2O6BSOMhpcwApQZdZZngV9K45jIsc_iVCsIo&amp;hash=Acq7ioDxHR5l1iZ8"
    ###fb = requests.post(url='https://graph.facebook.com/985618928451302/videos', data=m, headers={'Content-Type': m.content_type} )
    #fb = requests.post('https://graph.facebook.com/985618928451302/photos', data=data ) # ITS WORK!!!
    fb = requests.post('https://graph.facebook.com/1431304253689661/photos', data=data ) # ITS WORK!!!
    data2 = [
        # ('url', 'https://www.facebook.com/images/fb_icon_325x325.png'),  # url вашей фотографии
        # ('url', 'https://avatars.mds.yandex.net/get-pdb/1522705/c0ae8580-efcd-46c5-a94b-e9a2636d599c/s1200'),  # url вашей фотографии
        ('source', href),  # url вашей фотографии
        #('caption', 'Test text'),  # любой ваш текст который хотите публиковать
        ('access_token', access_token),  # ну и токен куда мы без него
        # ('content-type', 'video/mp4')
    ]
    #fb = requests.post('https://graph.facebook.com/985618928451302/', data=data2 ) # ITS NOT WORK YET!!!
    print(fb.text)
    ######################################## Рабочая версия!!!
    # graph.put_object(985618928451302, "feed", message="тест", attachments='photo'+photo_url) #так выкладываем объект, в нашем случае текст
    # graph.put_object(985618928451302, "feed", message="тест", source=photo_url) #так выкладываем объект, в нашем случае текст
    # graph.put_object(985618928451302, "feed", message="тест", source=photo.read()) #так выкладываем объект, в нашем случае текст
    # photo.close()
    # to get your posts/feed
    feed = graph.get_connections("me", "feed")
    post = feed["data"]
    print(post)
#https://www.facebook.com/connect/login_success.html#access_token=EAAHh0PN7IvABAD0AbFYZAdsMZAB8RRqWIT1LrJ5iy1Yc1MZAS8h9kZCzLOizFZAmpZAOlBTZA9HU9IZADCrFuPjyin2o3LIdmvumiIdwG2qsvKA7r9hZBTvUGjmyVj3NQ0SzTwfx6orNizNndA5FEE6Vriyq2ua5PHJAGSBb6tZAnkg4zRQSRZB05jp2pfKXGW5Re8ZD&data_access_expiration_time=1582991234&expires_in=4366
def auth():
    parse_url = 'https://www.facebook.com/connect/blank.html#_=_'
    app_id = "529762531091184"
    canvas_url = 'https://www.facebook.com/connect/login_success.html'#"https://vk.me/public187864217"
    redir_url = "https://vk.me/public187864217"
    perms = ["manage_pages", "publish_pages", "pages_manage_cta", "pages_show_list", "pages_messaging", "business_management", "pages_manage_instant_articles"]
    fb_auth_redirect_url2 = "https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=manage_pages"
    fb_auth_redirect_url2 = "https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=manage_pages,publish_pages,pages_manage_cta,pages_show_list,pages_messaging,business_management,pages_manage_instant_articles&response_type=token"
    fb_auth_redirect_url2 = "https://www.facebook.com/dialog/oauth?client_id=529762531091184&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=manage_pages,publish_pages&response_type=token&enable_profile_selector=1&profile_selector_ids=pageid"
    x1 = webbrowser.open(fb_auth_redirect_url2, new=0, autoraise=False)
    tttoken = 'EAAHh0PN7IvABAHY3tRpZCbsZA38IFx504PLiZBjGP3DeXvKd18MkhKLpnhRy4POv9LBt2WrkZBMfnG3LZCKwfZC2G48P6ktk2ciKXODpqquaTxYlmfd0EYSxu7WO83x7wGC0cbqpjnZCHeBukH1CtunTPwWxVlvOCc4NZC200aYhvAlYESwgB8UQce3ruDjeGVgZD'
    tttoken = 'EAAHh0PN7IvABAD0AbFYZAdsMZAB8RRqWIT1LrJ5iy1Yc1MZAS8h9kZCzLOizFZAmpZAOlBTZA9HU9IZADCrFuPjyin2o3LIdmvumiIdwG2qsvKA7r9hZBTvUGjmyVj3NQ0SzTwfx6orNizNndA5FEE6Vriyq2ua5PHJAGSBb6tZAnkg4zRQSRZB05jp2pfKXGW5Re8ZD'
    print(tttoken)
    l_token = requests.get("https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id="+fb_app_id+"&client_secret="+fb_secret+"&fb_exchange_token="+tttoken )
    print(l_token.json()['access_token'])
    print(x1)
    '''token = l_token.json()['access_token'] #Здесь получаем долгосрочный токен
    photo = 'https://sun9-21.userapi.com/c849532/v849532916/193b25/qd2H-t58ywo.jpg'#photo_url  # photo_vk_dialig_url
    print(token)
    data = [
        ('url', photo),  # url вашей фотографии
        ('caption', 'Новая публикация'),  # любой ваш текст который хотите публиковать
        ('access_token', token),  # ну и токен куда мы без него
    ]
    fb = requests.post('https://graph.facebook.com/985618928451302/photos', data=data ) # ITS WORK!!!
    print(fb.text)'''

def fb_get_groups():
    r = requests.get("https://graph.facebook.com/v5.0/me?fields=id,groups{administrator}&access_token=EAAHh0PN7IvABANYp4AGZACdSGGI0OiiQC0UFA8BYvl6q0LaLZBg22aFRXlUpXTmF0rBkf5RxAZCCLqCZCEp2ZB8E0n3ZCsbH6NZAZCNAMriefcZBsNuIPkydOk8txTrhUsBTw7ZBVZAs4vGOOankNWkwOnY5hmsM7bRYr8ZD")
    #print(r.json()['groups'])
    r = r.json()['groups']['data']
    print(r)
    #mass = []
    #mass = json.loads(r.read())
    for ind in r:
        if (ind['administrator'] == True):
            print (ind['id'])

import re
def get_token_from_url(url):
    #a = 'https://www.facebook.com/connect/login_success.html#access_token=EAAHh0PN7IvABAKVgKTNZAKf6WKZBf011Cv4arYEHC0UpwTwdyGGIZAGuz0CAVEivz9rZCfihrV8shvZCvvJd4qPgAbnQNHaspuhgWitgMuCseqKKY1X45dhXBzhehxgy2ZBN64nZBKTuUWN8lQtiqOra3kGSB9kgssI9sxgrieBZCWJBLxs6f8VbMZAA4FRuzZAZB0ZD&data_access_expiration_time=1582990511&expires_in=5089'
    url = re.search("(?P<url>access_token=[\w]+)",url).group("url")
    url = url.split('=')[1]
    print (url)
    #print (re.search("(?P<url>access_token=[\w]+)", a).group("url"))


#facebook_posting()
#vk_posting() #https://www.facebook.com/connect/login_success.html#access_token=EAAHh0PN7IvABAKVgKTNZAKf6WKZBf011Cv4arYEHC0UpwTwdyGGIZAGuz0CAVEivz9rZCfihrV8shvZCvvJd4qPgAbnQNHaspuhgWitgMuCseqKKY1X45dhXBzhehxgy2ZBN64nZBKTuUWN8lQtiqOra3kGSB9kgssI9sxgrieBZCWJBLxs6f8VbMZAA4FRuzZAZB0ZD&data_access_expiration_time=1582990511&expires_in=5089
#tmp_func()
#auth()
#get_token_from_url('https://www.facebook.com/connect/login_success.html#access_token=EAAHh0PN7IvABAKVgKTNZAKf6WKZBf011Cv4arYEHC0UpwTwdyGGIZAGuz0CAVEivz9rZCfihrV8shvZCvvJd4qPgAbnQNHaspuhgWitgMuCseqKKY1X45dhXBzhehxgy2ZBN64nZBKTuUWN8lQtiqOra3kGSB9kgssI9sxgrieBZCWJBLxs6f8VbMZAA4FRuzZAZB0ZD&data_access_expiration_time=1582990511&expires_in=5089')
#fb_get_groups()
#fb_post_photo(photo_url2,'текст','EAAHh0PN7IvABANYp4AGZACdSGGI0OiiQC0UFA8BYvl6q0LaLZBg22aFRXlUpXTmF0rBkf5RxAZCCLqCZCEp2ZB8E0n3ZCsbH6NZAZCNAMriefcZBsNuIPkydOk8txTrhUsBTw7ZBVZAs4vGOOankNWkwOnY5hmsM7bRYr8ZD')

'''while True:
    data = conn.recv(1024)
    if not data:
        break
    #conn.send(data.upper())
    print('test')

    if (data == bytes('1',encoding='UTF-8')):
        facebook_posting()
    elif (data == bytes('2',encoding='UTF-8')):
        vk_posting()

conn.close()'''




