import unittest
from Classes.service import Service
from Classes.repository import Repository


class TestService(unittest.TestCase):
    def test_init_service(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = Repository(access_token, http_string)
        service = Service(rep)
        self.assertEqual(service.repository.http_string, http_string)
        self.assertEqual(service.repository.access_token, access_token)

    def test_what_age(self):
        service = Service(Repository('irina', 'http'))
        before2019 = service.what_age(1998)
        after2019 = service.what_age(3000)
        self.assertEqual(before2019, 21)
        self.assertEqual(after2019, None)