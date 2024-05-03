import requests

place_names = ['London', 'svo', 'Череповец']
for place in place_names:
    url = f'https://wttr.in/{place}'
    params = {'nTqm': '', 'lang': 'ru', 'M': ''}
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)