#python -m unittest -v TestUser.py TestMyRepository.py TestRepository.py TestRepositoryIsolation.py TestService.py TestServiceIsolation.py TestUser.py
#coverage run -m unittest TestUser.py TestMyRepository.py TestRepository.py TestRepositoryIsolation.py TestService.py TestServiceIsolation.py TestUser.py
#coverage report -m

import requests
import json
from Classes.moc_repository import MocRepository
from Classes.service import Service
#https://oauth.vk.com/blank.html#access_token=e08467d24e10ac132bb3962ba33ba3903947101733179a47a86160d1d8494106a325fe1cfeeb5a20a2da8&expires_in=0&user_id=136006081&email=serzh_bessonov@mail.ru

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
print('lklk')