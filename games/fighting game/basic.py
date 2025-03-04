import random



#player
class player:
    def __init__(self):
        self.hp=100
        self.power=100
    
    def punch(self,enemy):
        if self.power<=10:
            return False
        else:
            enemy.hp-=10
            self.power-=10
    
    def kick(self,enemy):
        if self.power<=20:
            return False
        else:
            enemy.hp-=20
            self.power-=20

    def hp_checker(self):
        if self.hp<=0:
            return False
        return True

#enemy
class enemy:
    def __init__(self,level):
        self.level=level
        self.hp=100*level
        self.atk=5*level
        self.drop=1+level
    
    def attack(self,player):
            player.hp-=self.atk
            iteam=random.randint(1,self.drop)
            if iteam==1:
                player.hp+=(10+(self.drop/2))
                return "You get +10 HP"
            elif iteam==2:
                player.power+=(5+(self.drop/2))
                return "You get Power"
            elif iteam==3:
                player.hp+=20
                player.power+=10
                return "You get +20 HP +10 Power"
            else:
                return "You get nothing :("
    
    def hp_checker(self):
        if self.hp<=0:
            return False
        return True


