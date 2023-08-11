class Player:
    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health
        self.attack = 10
        self.items = []
        self.weapons = []
        self.equepment = None
        self.last_move = None

def pick_up_item(self, item):
    self.items.append[item]
    print(f"you have picked up {item.name}")

def pick_up_weaapon(self, weapons):
        self.items.append[weapons]
        print(f"You have picked up {weapons.name}")

def use_item(self, item):
     if item in self.items:
          self.health =+ item.use()
          print(f"current health: {self.health}")
          self.items.remove(item)

def equep_weapon(self, weapon):
     if weapon in self.weapon:
          self.health =+ weapon.use()
          print(f"your attacks now do {self.attack} damage")
          self.items.remove(weapon)

