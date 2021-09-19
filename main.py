import requests

class Hero:
    def __init__(self, name):
        self.name = name
    def get_intelligence(self):
        url = 'https://superheroapi.com/api/2619421814940190/search/' + self.name
        response = requests.get(url, timeout=5)
        hero_stats = response.json()
        intelligence = hero_stats.get('results')[0].get('powerstats').get('intelligence')
        return intelligence

def max_intelligence(hero_list):
    max_int = 0
    max_int_name = None
    for hero in hero_list:
        if int(hero.get_intelligence()) > int(max_int):
            max_int = hero.get_intelligence()
            max_int_name = hero.name
    print(f'Самый умный герой: {max_int_name} с показателем intelligence {max_int}')

hulk = Hero('Hulk')
captain_america = Hero('Captain America')
thanos = Hero('Thanos')

max_intelligence([hulk, captain_america, thanos])












