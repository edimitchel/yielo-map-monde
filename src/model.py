import json

class MapModel():
    def __init__(self):
        self.usersConnected = []

    def addUser(self, userInfo):
        user = {}
        user['id'] = userInfo['id_user']
        user['position'] = {}
        user['position']['latitude'] = userInfo['geolocalisation']['la']
        user['position']['longetitude'] = userInfo['geolocalisation']['lo']
        self.usersConnected.append(user)
        return user

    def getUsersConnected(self):
        return self.usersConnected
