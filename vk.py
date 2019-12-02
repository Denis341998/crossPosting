#import vk
import requests
#import urllib.request


token = "a20cd6f945993dbe3aa20b52c1b4a9da621779b2f5238b9d789364d02cdd27463d731701b3580002dad72"

id_group = 187864217
id_user = 99355143
app_id = 7156870
client_secret = '9nwdqTtxoA3Whp04mnbY'

redirect_uri = 'http://api.vk.com/blank.html'
v = 5.103

#session = vk.Session(access_token = token)
#api = vk.API(session)




def test_auth():
    tok = requests.get("https://oauth.vk.com/authorize", params={'client_id': app_id,
                                                                    'display': 'page',
                                                                    'redirect_uri': redirect_uri,
                                                                    'scope': 'wall,groups,friends,photos',
                                                                    'response_type': 'token',
                                                                    'v': v
                                                                    }).json()

    return tok['access_token']


def auth():
# OFFLINE не забыть

#us: https://oauth.vk.com/authorize?client_id=7156870&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall,groups,friends,photos&response_type=token&v=5.103
#gr: https://oauth.vk.com/authorize?client_id=7156870&group_ids=187864217&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall,photos&response_type=token&v=5.103

#https://oauth.vk.com/authorize?client_id=7156870&display=page&redirect_uri=http://api.vk.com/blank.html&scope=wall,groups,friends,photos&response_type=code&v=5.103
#https://oauth.vk.com/access_token?client_id=7156870&client_secret=9nwdqTtxoA3Whp04mnbY&redirect_uri=http://api.vk.com/blank.html&code=337b702f27333926fd

    code = requests.get("https://oauth.vk.com/authorize", params={'client_id': app_id,
                                                                  'display': 'page',
                                                                  'redirect_uri': redirect_uri,
                                                                  'scope': 'wall,groups,friends,photos',
                                                                  'response_type': 'code',
                                                                  'v': v
                                                                  }).json()

    tok = requests.get("https://oauth.vk.com/access_token", params={'client_id': app_id,
                                                                   'client_secret': client_secret,
                                                                   'redirect_uri': redirect_uri,
                                                                   'code': code['code']
                                                                   }).json()

    return tok['access_token']


def take_groups():         # OK

    grs = requests.get("https://api.vk.com/method/groups.get", params = {'access_token': token,
                                                                          'user_id': id_user,
                                                                          'extended': 1,
                                                                          'filter': 'admin',
                                                                          # 'fields': 'name',
                                                                          'v': v
                                                                         }).json()

    ids = []
    names = []
    cnt = grs['response']['count']

    for i in range (cnt):
        ids.append(grs['response']['items'][i]['id'])
        names.append(grs['response']['items'][i]['name'])

    data = [ids, names]

    return data


def take_posts():        # OK

    #req = "https://api.vk.com/method/wall.get?access_token=  &v=5.103&owner_id=-187864217&count=1"

    g = id_group * (-1)

    response = requests.get("https://api.vk.com/method/wall.get", params = {'access_token': token,
                                                                            'v': v,
                                                                            'owner_id': g,
                                                                            'count': 2
                                                                           }).json()

    data = response['response']['items']

    return data


def make_post():        # OK

    #req = "https://api.vk.com/method/wall.post?access_token=  &v=5.103&domain=prin66"

    g = id_group * (-1)

    data = requests.get("https://api.vk.com/method/wall.post", params = {'access_token': token,
                                                                         'v': v,
                                                                         'owner_id': g,
                                                                         'from_group': 1,
                                                                         'attachments': 'photo99355143_457247901',
                                                                         'message': 'TEST WALL POST'
                                                                        }).json()
    return data


def savePhotoToServ(str):        # OK

    #str - 'V://I//1.jpg'  /  '1.jpg'
    s1 = requests.get("https://api.vk.com/method/photos.getWallUploadServer", params={'access_token': token,
                                                                                      'v': v,
                                                                                      'group_id': id_group
                                                                                      }).json()

    upload_url = s1['response']['upload_url']

    file = {'file1': open(str, 'rb')}
    upload_resp = requests.post(upload_url, files=file).json()

    s2 = requests.get("https://api.vk.com/method/photos.saveWallPhoto", params={'access_token': token,
                                                                                'v': v,
                                                                                'group_id': id_group, # upload_resp['gid']
                                                                                'photo': upload_resp['photo'],
                                                                                'server': upload_resp['server'],
                                                                                'hash': upload_resp['hash']
                                                                                }).json()

    return s2


def make_post_with_photo(*ph):          #OK

    #str's with adresses of photos

    str = ''

    for x in ph:
        s2 = savePhotoToServ(x)

        owner_id = s2['response'][0]['owner_id'].__str__()
        id = s2['response'][0]['id'].__str__()

        str += 'photo'+owner_id+'_'+id+','

    str = str[:-1]
    g = id_group * (-1)

    data = requests.get("https://api.vk.com/method/wall.post", params = {'access_token': token,
                                                                         'v': v,
                                                                         'owner_id': g,
                                                                         'from_group': 1,
                                                                         'attachments': str,
                                                                         'message': 'TEST WALL POST'
                                                                        }).json()

    return data



def get_photo_url(*ids):
    """ Получаем прикрепленное фото"""
    # ph = photo['sizes'][6]['url']
    # id_mes = requests.get('https://api.vk.com/method/messages.get', params={'access_token': self.tok,
    #                                                                          'v': self.v,
    #                                                                          # 'message_ids': ,
    #                                                                          'extended': 1,
    #                                                                          'group_id': self.id_group
    #                                                                         }).json()

    # mes = requests.get("https://api.vk.com/method/messages.getById", params={'access_token': token,
    #                                                                          'v': v,
    #                                                                          'message_ids': ids,
    #                                                                          'extended': 1,
    #                                                                          'group_id': id_group
    #                                                                         }).json()

    # ph = mes['response']['items']['attachments']['photo']['id']

    # return ph


# ----------------------------------------------------------------------------------------------------------


#data = make_post_with_photo('1.jpg', '2.jpg', '3.jpg')
# data = make_post()
# data = make_post_with_photo('C:/Users/User/Desktop/Vicky/MKP/bot_new/1.jpg')
# data = get_photo_url(893969)
# data = take_groups()
print(1)



