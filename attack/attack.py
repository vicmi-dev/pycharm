from classes.enemy import Enemy


enemy = Enemy(200,60)
print("HP", enemy.get_hp())
















'''import random

class Enemy:
    hp = 200

    def __init__(self,atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("atk is", self.atkl)

    def getHp(self):
        print("Hp is", self.hp)
        
enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()
'''
'''hjas dfvak sdvaj sthis is comment and i can write
whatever i want to, okay that's perfect and enough'''

#everything here is a comment too

'''

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp > 30:
        continue

    print("You have low health. You've been teleported to the nearest inn.")
    break

'''