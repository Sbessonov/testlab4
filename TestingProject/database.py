from Classes.user import User

# =========================================== users.get
true_user_irina = User(6)

user_irina = {'response':
                  [{'id': 6,
                    'first_name': 'Ирина',
                    'last_name': 'Браткова',
                    'is_closed': False,
                    'can_access_closed': True,
                    'bdate': '6.11.1902'}]
              }

user_pavel = {'response':
                  [{'id': 1,
                    'first_name': 'Павел',
                    'last_name': 'Дуров',
                    'is_closed': False,
                    'can_access_closed': True,
                    'bdate': '10.10.1984'}]
              }

user_incognito = {'response':
                      [{'id': 777,
                        'first_name': 'Светочка',
                        'last_name': 'Незина',
                        'is_closed': False,
                        'can_access_closed': True}]
                  }

# =====================
# == friends.get

count_friends_irina = 10
friends_irina = {'response':
                     {'count': 10, 'items':
                         [{'id': 10,
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
                           'online': 1},
                          {'id': 20,
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
                           'online': 1},
                          {'id': 30,
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
                           'online': 1},
                          {'id': 656,
                           'first_name': 'Ольга',
                           'last_name': 'Вайнер',
                           'is_closed': False,
                           'can_access_closed': True,
                           'domain': 'olga_jas',
                           'online': 1}
                          ]
                      }
                 }

count_friends_pavel = 0
friends_pavel = {'response': {'count': 0, 'items': []}}

user_ban = {'error':
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

user_private = {'error':
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

# a = [i for i in range(10)]
# print(a[0:15])
# # tmp = friends_irina
# # tmp['response']['items'] = tmp['response']['items'][0:1]
# print(tmp)
