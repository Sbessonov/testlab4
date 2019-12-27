import requests


class Repository:
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
        return requests.get(self.url)