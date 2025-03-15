import random
from random import randrange
team = ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
def generate_random_list():
    random_list = random.sample(range(22), 22)
    return random_list
random_list = generate_random_list()
class Man:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return f'His name is {self.name}'

class Footballist(Man):
    def get_team(self):
        team_footballist = team[random_list[0]]
        del random_list[0]
        return f'His team is {team_footballist}'
def get_info():
    final = ''
    hossein = Footballist('Hossein')
    final += hossein.get_name()+ ' and '+  hossein.get_team()+ '\n'
    maziar = Footballist('Maziar')
    final += maziar.get_name()+ ' and '+ maziar.get_team()+ '\n'
    akbar = Footballist('Akbar')
    final += akbar.get_name()+ ' and '+ akbar.get_team()+ '\n'
    nima = Footballist('Nima')
    final += nima.get_name()+ 'and'+ nima.get_team()+ '\n'
    mehdi = Footballist('Mehdi')
    final += mehdi.get_name()+ ' and '+ mehdi.get_team()+ '\n'
    farhad = Footballist('Farhad')
    final += farhad.get_name()+ ' and '+ farhad.get_team()+ '\n'
    mohammad = Footballist('Mohammad')
    final += mohammad.get_name()+ ' and '+ mohammad.get_team()+ '\n'
    khashayar = Footballist('Khashayar')
    final += khashayar.get_name()+ ' and '+ khashayar.get_team()+ '\n'
    milad = Footballist('Milad')
    final += milad.get_name()+ ' and '+ milad.get_team()+ '\n'
    mostafa = Footballist('Mostafa')
    final += mostafa.get_name()+ ' and '+ mostafa.get_team()+ '\n'
    amin = Footballist('Amin')
    final += amin.get_name() + ' and '+ amin.get_team()+ '\n'
    saeed = Footballist('Saeed')
    final += saeed.get_name() + ' and '+ saeed.get_team()+ '\n'
    pouya = Footballist('Pouya')
    final += pouya.get_name() + ' and '+ pouya.get_team()+ '\n'
    pouria = Footballist('Pouria')
    final += pouria.get_name() + ' and '+ pouria.get_team()+ '\n'
    reza = Footballist('Reza')
    final += reza.get_name() + ' and '+ reza.get_team()+ '\n'
    ali = Footballist('Ali')
    final += ali.get_name() + ' and '+ ali.get_team()+ '\n'
    behzad = Footballist('Behzad')
    final += behzad.get_name()+ ' and '+ behzad.get_team()+ '\n'
    soheil = Footballist('Soheil')
    final += soheil.get_name()+ ' and '+ soheil.get_team()+ '\n'
    behrooz = Footballist('Behrooz')
    final += behrooz.get_name()+ ' and '+ behrooz.get_team()+ '\n'
    shahrooz = Footballist('Shahrooz')
    final += shahrooz.get_name() + ' and '+ shahrooz.get_team()+ '\n'
    saman = Footballist('Saman')
    final += saman.get_name()+ ' and '+ saman.get_team()+ '\n'
    mohsen = Footballist('Mohsen')
    final += mohsen.get_name()+ ' and '+ mohsen.get_team()+ '\n'
    return print(final)

get_info()

