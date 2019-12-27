#python -m unittest -v TestUser.py TestMyRepository.py TestRepository.py TestRepositoryIsolation.py TestService.py TestServiceIsolation.py TestUser.py
#coverage run -m unittest TestUser.py TestMyRepository.py TestRepository.py TestRepositoryIsolation.py TestService.py TestServiceIsolation.py TestUser.py
#coverage report -m

import requests
import json
from Classes.moc_repository import MocRepository
from Classes.service import Service

# urlUser = 'http://testvk.com/method/users.get?user_ids=6&fields=bdate&access_token=lab4&v=5.103'
# urlFrids = 'http://testvk.com/method/friends.get?user_id=6&count=5&fields=city,domain,bdate&access_token=lab4&v=5.103'
#
# response = requests.get(urlUser)
# print(response)
# print(response.text)
# print(json.loads(response.text))

access_token = 'irina'
http_string = 'http://irina/'
rep = MocRepository(access_token, http_string)
service = Service(rep)
users = service.get_friends_zodiacs(500, 10)

print(users)