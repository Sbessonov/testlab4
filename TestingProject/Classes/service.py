import enum
from Classes.user import User


class Service:
    def __init__(self, repository):
        self.repository = repository

    def what_age(self, year):
        return 2019 - year

    def get_friends_ages(self, user_id, count):
        pass

    def get_age(self, user_id):
        pass

    def __parse_user(self, response, user_id):
        pass

    def __pars_friensds(self, response, user_id):
        pass