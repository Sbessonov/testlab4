import unittest
from Classes.repository import Repository


# Тест репозитория при создании
class TestRepository(unittest.TestCase):
    def test_init_repository(self):
        rep = Repository('irina', 'http://patternvk.com')
        self.assertEqual(rep.http_string, 'http://patternvk.com')
        self.assertEqual(rep.access_token, 'irina')
        self.assertEqual(rep.url, '')

    def test_make_url_get_user(self):
        http_string = 'http://testvk.com'
        user_id = 10
        access_token = 'lab4'
        rep = Repository(access_token, http_string)
        self.assertEqual(rep.http_string, http_string)
        self.assertEqual(rep.access_token, access_token)
        self.assertEqual(rep.url, '')
        url = http_string
        url += '/method/'
        url += 'users.get?'
        url += 'user_ids=' + str(user_id)
        url += '&fields=bdate&'
        url += 'access_token=' + access_token
        url += '&v=5.103'
        rep.getUser(user_id)
        self.assertEqual(url, rep.url)

    def test_make_url_get_friends(self):
        http_string = 'http://testvk.com'
        user_id = 10
        count = 10
        access_token = 'lab4'
        rep = Repository(access_token, http_string)
        self.assertEqual(rep.http_string, http_string)
        self.assertEqual(rep.access_token, access_token)
        self.assertEqual(rep.url, '')
        url = http_string
        url += '/method/'
        url += 'friends.get?'
        url += 'user_id=' + str(user_id) + '&'
        url += 'count=' + str(count)
        url += '&'
        url += 'fields=city,domain,bdate&'
        url += 'access_token=' + access_token + '&v=5.103'
        rep.getFriends(user_id, count)
        self.assertEqual(url, rep.url)
