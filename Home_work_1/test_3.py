import requests
import yaml

# with open('enter.yaml') as f:
#     data = yaml.safe_load(f)
# url = data['url_post']
# title = data['title']
# description = data['description']
# content = data['content']
#
#
# def create_post(token):
#     p = requests.post('https://test-stand.gb.ru/gateway/posts', headers={'X-Auth-Token': token},
#                       data={'title': title, 'description': description, 'content': content})
#     return p.json()
#
#
# def findpost(token):
#     d = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
#     listdescript = [i['description'] for i in d.json()['data']]
#     return listdescript
#
#
# def test_3(login, text2):
#     assert text2 in findpost(login)
