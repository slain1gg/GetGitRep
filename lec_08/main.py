

class Monster:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0



    def talk(self):
        if self.is_alive():
            print(f'{self.name}: "My health {self.health}. Hit me!"')
        else:
            print(f'{self.name}: *dead*')


def main():

    monsters_list = [Monster('Alli'), Monster('Peno')]
    finished = False
    while not finished:
        monster = monsters_list[0]
        monster.talk()
        damage = int(input())
        monster.get_damage(damage)
        if not monster.is_alive():
            monster.talk()
            monsters_list.pop(0)
        if not monsters_list:
            finished = True

main()