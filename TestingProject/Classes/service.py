import enum
from Classes.user import User


class Service:
    def __init__(self, repository):
        self.repository = repository

    def what_age(self, year):
        return 2019 - year if year <= 2019 else None

    def get_friends_ages(self, user_id, count):
        response = self.repository.getFriends(user_id, count)
        user = self.__pars_friensds(response.text, user_id)
        if user.user_id == -1:
            return 'Не удалось получить список друзей'
        else:
            if len(user.list_friends) == 0:
                return 'У пользователя нет друзей'
            else:
                for friend in user.list_friends:
                    if friend.birth_date is None:
                        friend.age = 'Unknown'
                    else:
                        date = friend.birth_date
                        date = date.split('.')
                        friend.age = self.what_age(int(date[2]))
                return user.list_friends

    def get_age(self, user_id):
        response = self.repository.getUser(user_id)
        user = self.__parse_user(response.text, user_id)
        if user.birth_date is not None:
            date = user.birth_date
            date = date.split('.')
            user.age = self.what_age(int(date[2]))
        else:
            user.age = 'Дата рождения отсутствует'
        return user.age

    def __parse_user(self, response, user_id):
        answer = response['response']
        answer = answer[0]
        if user_id == int(answer['id']):
            user = User(user_id)
            user.first_name = answer['first_name']
            if user.first_name != 'DELETED':
                user.last_name = answer['last_name']
                try:
                    user.birth_date = answer['bdate']
                except KeyError:
                    user.birth_date = None
            user.list_friends = None
            return user

    def __pars_friensds(self, response, user_id):
        try:
            answer = response['response']
            items = answer['items']
            lst = []
            for tmp in items:
                newUser = User(int(tmp['id']))
                newUser.first_name = tmp['first_name']
                if newUser.first_name != 'DELETED':
                    newUser.last_name = tmp['last_name']
                    newUser.domain = tmp['domain']
                    try:
                        newUser.birth_date = tmp['bdate']
                    except KeyError:
                        newUser.birth_date = None
                    try:
                        newUser.city = tmp['city']['title']
                    except KeyError:
                        newUser.city = None
                lst.append(newUser)
            user = User(user_id)
            user.list_friends = lst
            return user
        except KeyError:
            return User(-1)