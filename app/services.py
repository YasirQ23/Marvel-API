import requests as r


class Pokemon_Info():
    def __init__(self, name):
        self.name = name
        self.weight = int
        self.ability = []
        self.type = []
        self.pic = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{name}.png'

    def getandlabel(self):
        request = r.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        self.request = request.json()

    def sort_poke(self):
        self.weight = int(self.request['weight']*.220462)
        self.name = self.request['forms'][0]['name'].title()
        for i in range(len(self.request['abilities'])):
            self.ability.append(
                self.request['abilities'][i]['ability']['name'].title())
        for i in range(len(self.request['types'])):
            self.type.append(self.request['types'][i]['type']['name'].title())
        self.info = {'Name': self.name, 'Type': self.type,
                     'Abilities': self.ability, 'Wegiht': self.weight}

    def poke_info(self):
        self.card = {'Name': self.name.title(), 'Type': self.type,
                     'Ability': self.ability, 'Weight': self.weight}


def lib_creation():
    poke_list = {}
    for i in range(1,10):
        poke_card = Pokemon_Info(i)
        poke_card.getandlabel()
        poke_card.sort_poke()
        poke_list[poke_card.name] = poke_card
    return poke_list