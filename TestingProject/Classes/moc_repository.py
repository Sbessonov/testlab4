import requests
import re
from Classes.response import Response
from database import *


class MocRepository:
    def __init__(self, access_token, http_string):
        self.access_token = access_token
        self.http_string = http_string
        self.url = ''
        self.method = ''

    def getUser(self, user_id):
        url = self.http_string
        url += '/method/'
        url += 'users.get?'
        self.method = 'users.get'
        url += 'user_ids=' + str(user_id)
        url += '&fields=bdate&'
        url += 'access_token=' + self.access_token
        url += '&v=5.103'
        self.url = url
        return self.get()

    def getFriends(self, user_id, count):
        url = self.http_string
        url += '/method/'
        url += 'friends.get?'
        self.method = 'friends.get'
        url += 'user_id=' + str(user_id) + '&'
        url += 'count=' + str(count)
        url += '&'
        url += 'fields=city,domain,bdate&'
        url += 'access_token=' + self.access_token + '&v=5.103'
        self.url = url
        return self.get()

    def get(self):
        if self.method == 'users.get':
            user_id = self.__pars_url_get_user()
            return self.__user_choice(user_id)
        elif self.method == 'friends.get':
            info = self.__pars_url_get_friends()
            return self.__friends_choice(int(info[0]), int(info[1]))

    def __friends_choice(self, user_id, count):
        if user_id == 6:
            tmp = friends_irina  # count = 10, запрашиваем 15
            resp = tmp['response']
            lst = resp['items']
            lst = lst[0:count]
            tmp['response']['items'] = lst
            response = Response()
            response.text = tmp
            response.status_code = 200
            return response
        elif user_id == 1:
            response = Response()
            response.text = friends_pavel
            response.status_code = 200
            return response
        elif user_id == 9:  # permach ban
            response = Response()
            response.text = user_ban
            response.status_code = 200
            return response
        else:
            response = Response()
            response.text = user_private
            response.status_code = 200
            return response

    def __pars_url_get_user(self):
        url = self.url
        user_ids = re.search('user_ids=', url)
        if user_ids:
            index = url.find('user_ids=')
            if index != -1:
                indexBegin = index + len('user_ids=')
                indexEnd = url.find('fields') - 1  # находим &
                user = ''
                while indexBegin < indexEnd:
                    user += url[indexBegin]
                    indexBegin += 1
                return int(user)

    def __pars_url_get_friends(self):
        url = self.url
        user_ids = re.search('user_id=', url)
        if user_ids:
            index = url.find('user_id=')
            if index != -1:
                indexBegin = index + len('user_id=')
                indexEnd = url.find('count=')  # находим &
                user = ''
                while indexBegin < indexEnd - 1:
                    user += url[indexBegin]
                    indexBegin += 1
                indexEnd += len('count=')
                indexBegin = indexEnd
                indexEnd = url.find('fields=')
                count = ''
                while indexBegin < indexEnd - 1:
                    count += url[indexBegin]
                    indexBegin += 1
                return int(user), int(count)

    def __user_choice(self, user_id):
        if user_id == 6:
            response = Response()
            response.text = user_irina
            response.status_code = 200
            return response
        elif user_id == 1:
            response = Response()
            response.text = user_pavel
            response.status_code = 200
            return response
        elif user_id == 777:
            response = Response()
            response.text = user_incognito
            response.status_code = 200
            return response
        else:
            response = Response()
            response.text = {'response':
                                 [{'id': user_id,
                                   'first_name': 'DELETED',
                                   'last_name': '',
                                   'deactivated': 'deleted'}]
                             }
            response.status_code = 200
            return response
