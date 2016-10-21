class player:
    def _init_(self):
        self.name = ""
        self.health = 1
        self.health_max = 100
    def do_damage(self,enemy):
        damage = min(
            max(radiant(0, self.heath) - radiant(0, enemy.health)1),
            enemy.health)
        enemy.health = enemy.health - damage
        if damage == 0: print"%s evades %s's attack."%(enemy.name, self.name)
        else: print "%s hurts %s!" % (self.name, enemy.name)
        return enemy.health <= 0
