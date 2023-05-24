import requests





def get(token):
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    listcount = [i['content'] for i in g.json()['data']]
    return listcount


def test_step2(login, text1):
    assert 'Сдесь могла бы быть ваша реклама)' in get(login)