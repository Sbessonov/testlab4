import unittest
from Classes.service import Service
import Classes.moc_repository as moc_repo


class TestServiceIsolation(unittest.TestCase):
    def test_init_service(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = moc_repo.MocRepository(access_token, http_string)
        service = Service(rep)
        self.assertEqual(service.repository.http_string, http_string)
        self.assertEqual(service.repository.access_token, access_token)

    def test_get_age_irina(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = moc_repo.MocRepository(access_token, http_string)
        service = Service(rep)
        age = service.get_age(6)
        self.assertEqual(117, age)

    def test_not_get_age(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = moc_repo.MocRepository(access_token, http_string)
        service = Service(rep)
        age = service.get_age(666)
        self.assertEqual('Дата рождения отсутствует', age)

    def test_get_age_pavel(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = moc_repo.MocRepository(access_token, http_string)
        service = Service(rep)
        age = service.get_age(1)
        self.assertEqual(35, age)

    def test_get_age_incognito(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = moc_repo.MocRepository(access_token, http_string)
        service = Service(rep)
        age = service.get_age(777)
        self.assertEqual('Дата рождения отсутствует', age)

    def test_get_pavel_friends_ages(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = moc_repo.MocRepository(access_token, http_string)
        service = Service(rep)
        ages = service.get_friends_ages(1, 666)
        self.assertEqual('У пользователя нет друзей', ages)

    def test_get_irina_friends_ages(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = moc_repo.MocRepository(access_token, http_string)
        service = Service(rep)
        usesr = service.get_friends_ages(6, 10)
        true_ages = [112, 112, 112, 'Unknown']
        new_ages = [usesr[0].age, usesr[1].age, usesr[2].age, usesr[3].age]
        self.assertEqual(true_ages, new_ages)

    def test_get_ban_friends_age(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = moc_repo.MocRepository(access_token, http_string)
        service = Service(rep)
        usesr = service.get_friends_ages(9, 10)
        answer = 'Не удалось получить список друзей'
        self.assertEqual(usesr, answer)

    def test_get_private_friends_age(self):
        access_token = 'irina'
        http_string = 'http://irina/'
        rep = moc_repo.MocRepository(access_token, http_string)
        service = Service(rep)
        users = service.get_friends_ages(500, 10)
        answer = 'Не удалось получить список друзей'
        self.assertEqual(users, answer)