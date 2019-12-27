import unittest
import socketserver
from server import MyHandler


class TestMyServer(unittest.TestCase):
    def test_init(self):
        url = '10'
        self.assertEqual('10', url)

    def test_pars_url_user_get(self):
        handler = MyHandler
        handler.path = '/method/users.get?user_ids=1'
        method = 'method'
        usersGet = 'users.get'
        userIds = 'user_ids='
        handler.pars_url(MyHandler)
        self.assertEqual(method, handler.testList[0])
        self.assertEqual(usersGet, handler.testList[1])
        self.assertEqual(userIds, handler.testList[2])

    def test_pars_url_user_get_number_one(self):
        handler = MyHandler
        at = handler.access_token
        handler.path = '/method/users.get?user_ids=1&fields=bdate&access_token=lab4&v=5.103'
        method = 'method'
        usersGet = 'users.get'
        userIds = 'user_ids='
        user = '1'
        handler.pars_url(MyHandler)
        self.assertEqual(method, handler.testList[0])
        self.assertEqual(usersGet, handler.testList[1])
        self.assertEqual(userIds, handler.testList[2])
        # self.assertEqual(user, handler.user)

    def test_choise_user(self):
        handler = MyHandler
        # Дуров
        handler.user = '1'
        user = {'response':
                        [{'id': 1,
                          'first_name': 'Павел',
                          'last_name': 'Дуров',
                          'is_closed': False,
                          'can_access_closed': True,
                          'bdate': '10.10.1984'}]
                    }
        newUser = handler.user_choice(handler)
        self.assertEqual(user, newUser)
        # Браткова
        handler.user = '6'
        user = {'response':
                        [{'id': 6,
                          'first_name': 'Ирина',
                          'last_name': 'Браткова',
                          'is_closed': False,
                          'can_access_closed': True,
                          'bdate': '6.11.1902'}]
                    }
        newUser = handler.user_choice(handler)
        self.assertEqual(user, newUser)
        #Сатана
        handler.user = '666'
        user = {'response':
                        [{'id': 666,
                          'first_name': 'DELETED',
                          'last_name': '',
                          'deactivated': 'deleted'}]
                    }
        newUser = handler.user_choice(handler)
        self.assertEqual(user, newUser)

    def test_pars_url_user_get_friends(self):
        handler = MyHandler
        at = handler.access_token
        handler.path = '/method/friends.get?user_id=X&count=Y&fields=city,domain,bdate&access_token=Z&v=5.103'
        method = 'method'
        usersGet = 'friends.get'
        userIds = 'user_id='
        user = '1'
        handler.pars_url(MyHandler)
        self.assertEqual(method, handler.testList[0])
        self.assertEqual(usersGet, handler.testList[1])
        self.assertEqual(userIds, handler.testList[2])
        # self.assertEqual(user, handler.user)
