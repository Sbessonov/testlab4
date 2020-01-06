import unittest
import Classes.moc_repository as moc_rep


# Тест репозитория при создании
class TestMocRepository(unittest.TestCase):
    def test_init_my_repository(self):
        MocRepository = moc_rep.MocRepository('irina', 'http://test.vk')
        self.assertEqual('irina', moc_rep.MocRepository.access_token)
        self.assertEqual('http://test.vk', moc_rep.MocRepository.http_string)
        self.assertEqual('', moc_rep.MocRepository.url)

    def test_get_irina(self):
        moc_rep.MocRepository = moc_rep.MocRepository('irina', 'http://test.vk')
        user = moc_rep.MocRepository.getUser(6)
        true_user = {'response':
                         [{'id': 6,
                           'first_name': 'Ирина',
                           'last_name': 'Браткова',
                           'is_closed': False,
                           'can_access_closed': True,
                           'bdate': '6.11.1902'}]
                     }
        self.assertEqual(user.text, true_user)

    def test_get_pavel(self):
        moc_rep.MocRepository = moc_rep.MocRepository('irina', 'http://test.vk')
        user = moc_rep.MocRepository.getUser(1)
        true_user = {'response':
                         [{'id': 1,
                           'first_name': 'Павел',
                           'last_name': 'Дуров',
                           'is_closed': False,
                           'can_access_closed': True,
                           'bdate': '10.10.1984'}]
                     }
        self.assertEqual(user.text, true_user)

    def test_get_satan(self):
        moc_rep.MocRepository = moc_rep.MocRepository('irina', 'http://test.vk')
        user = moc_rep.MocRepository.getUser(999)
        true_user = {'response':
                         [{'id': 999,
                           'first_name': 'DELETED',
                           'last_name': '',
                           'deactivated': 'deleted'}]
                     }
        self.assertEqual(user.text, true_user)

    def test_get_happy_3friends(self):
        repo = moc_rep.MocRepository('irina', '')
        friends = repo.getFriends(6, 4)
        true_friends = {'response':
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
        self.assertEqual(true_friends, friends.text)

    def test_get_friends_pavel(self):
        repo = moc_rep.MocRepository('','')
        friends = repo.getFriends(1, 99)
        true_friends = {'response': {'count': 0, 'items': []}}
        self.assertEqual(true_friends, friends.text)

    def test_get_friends_ban(self):
        repo = moc_rep.MocRepository('', '')
        friends = repo.getFriends(9, 99)
        true_friends = {'error':
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
        self.assertEqual(true_friends, friends.text)

    def test_get_friends_private(self):
        repo = moc_rep.MocRepository('', '')
        friends = repo.getFriends(700, 99)
        true_friends = {'error':
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
        self.assertEqual(true_friends, friends.text)