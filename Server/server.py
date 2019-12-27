import http.server
import socketserver
import json
import re


class MyHandler(http.server.SimpleHTTPRequestHandler):
    access_token = 'lab4'
    testList = []
    user = ''
    method = ''
    count = ''
    flag = False

    # http://testvk.com/method/friends.get?user_id=X&count=Y&fields=city,domain,bdate&access_token=Z&v=5.103'
    # http://testvk.com/method/users.get?user_ids=X&fields=bdate&access_token=Y&v=5.103'

    def pars_url(self):
        url = self.path
        self.testList = []
        method = re.search('method', url)
        if method:
            self.testList.append(method[0])  # global[0] = method
            usersGet = re.search('users.get', url)
            friendsGet = re.search('friends.get', url)
            if usersGet:
                self.method = 'users.get'
                self.testList.append(usersGet[0])  # global[1] = users.get
                url = self.path
                user_ids = re.search('user_ids=', url)
                if user_ids:
                    self.testList.append(user_ids[0])  # global[2] = 'user_ids='
                    index = url.find('user_ids=')
                    if index != -1:
                        indexBegin = index + len('user_ids=')
                        indexEnd = url.find('fields') - 1  # находим &
                        user = ''
                        while indexBegin < indexEnd:
                            user += url[indexBegin]
                            indexBegin += 1
                        return user
            if friendsGet:
                self.method = 'friends.get'
                self.testList.append(friendsGet[0])  # global[1] = friends.get
                print(friendsGet, self.testList[1])
                user_ids = re.search('user_id=', url)
                if user_ids:
                    self.testList.append(user_ids[0])  # global[2] = 'user_id='
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
                        return user, count

    def user_choice(self):
        if self.user == '6':
            return {'response':
                        [{'id': 6,
                          'first_name': 'Ирина',
                          'last_name': 'Браткова',
                          'is_closed': False,
                          'can_access_closed': True,
                          'bdate': '6.11.1902'}]
                    }
        elif self.user == '1':
            return {'response':
                        [{'id': 1,
                          'first_name': 'Павел',
                          'last_name': 'Дуров',
                          'is_closed': False,
                          'can_access_closed': True,
                          'bdate': '10.10.1984'}]
                    }
        else:
            return {'response':
                        [{'id': int(self.user),
                          'first_name': 'DELETED',
                          'last_name': '',
                          'deactivated': 'deleted'}]
                    }

    def make_list_friends(self):
        count = int(self.count)
        if count > 1:
            i = 0
            lst = []
            while i < count:
                tmp = {
                    'id': i,
                    'first_name': 'Костя',
                    'last_name': 'Тумбаюмба',
                    'is_closed': False,
                    'can_access_closed': True,
                    'domain': 'kostya',
                    'bdate': '14.02.1945',
                    'city': {
                        'id': 1,
                        'title': 'Череповец'
                    },
                    'online': 1
                }
                lst.append(tmp)
                i += 1
            count = 100
            response = {'response':
                {
                    'count': count,
                    'items': lst
                }
            }
            return response
        elif count == 1:
            return {'response':
                        {'count': 250, 'items':
                            [{'id': 792687,
                              'first_name': 'Ольга',
                              'last_name': 'Вайнер',
                              'is_closed': False,
                              'can_access_closed': True,
                              'domain': 'olga_jas',
                              'bdate': '21.12.1945',
                              'city': {
                                  'id': 1,
                                  'title': 'Москва'
                              },
                              'online': 1}]
                         }
                    }
        else:
            return {'response': {'count': 0, 'items': []}}

    def friends_choice(self):
        if ((self.user == '1') or (self.user == '6')) and int(self.count) > 0:
            return self.make_list_friends()
        elif self.user == '9': # permach ban
            return {'error':
                    {'error_code': 18,
                     'error_msg': 'User was deleted or banned',
                     'request_params':
                         [{'key': 'user_id', 'value': '3'},
                          {'key': 'count', 'value': '0'},
                          {'key': 'fields', 'value': 'city,domain'},
                          {'key': 'v', 'value': '5.103'},
                          {'key': 'method', 'value': 'friends.get'},
                          {'key': 'oauth', 'value': '1'}]}
                }
        elif int(self.count) == 0:
            return {'response': {'count': 0, 'items': []}}
        else:
            return {'error':
                    {'error_code': 30,
                     'error_msg': 'This profile is private',
                     'request_params':
                         [{'key': 'user_id', 'value': '2'},
                          {'key': 'count', 'value': '0'},
                          {'key': 'fields', 'value': 'city,domain'},
                          {'key': 'v', 'value': '5.103'},
                          {'key': 'method', 'value': 'friends.get'},
                          {'key': 'oauth', 'value': '1'}
                          ]
                     }
                    }

    def do_GET(self):
        result = self.pars_url()
        if self.method == 'users.get':
            self.user = result
            result = self.user_choice()
            self.send_response(200)
            self.send_header('content', 'text')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            self.flag = True
        elif self.method == 'friends.get':
            self.user = result[0]
            self.count = result[1]
            result = self.friends_choice()
            self.send_response(200)
            self.send_header('content', 'text')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            self.flag = True
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)
