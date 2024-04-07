# player.py

import pygame
from creature import Creature
from monster import Monster
from equipment import Equipment, Potion, Coin

class Player(Creature):
    def __init__(self,x,y,map,blocks):
        super().__init__('player',x,y,map,blocks)
        self.rect.topleft = self.set_initial_pos()
        self.message_log = map.message_log
        self.dead = False
        self.speed = 2
        self.xp = 0
        self.max_xp_per_level = 10
        self.level = 0
        self.inventory = []
        self.inventory_size = 5
        self.coin = 0
        

    def set_initial_pos(self):
        room = self.map.get_initial_room()
        (x,y) = room.center()
        return (x * self.tile_size, y * self.tile_size)
    
    
    def input(self):
        # Calculate the next position of the player
        keys_pressed = pygame.key.get_pressed()
        next_rect = self.rect.copy()
        if keys_pressed[pygame.K_LEFT]:
            next_rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            next_rect.x += self.speed
        if keys_pressed[pygame.K_UP]:
            next_rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            next_rect.y += self.speed
        return next_rect

    def move(self):
    # Check for collision with walls
        dest = self.input()
        if not self.check_collision(dest) and self.moves:
            self.rect = dest
        

    def meet(self, entity):
        if isinstance(entity, Monster):
            self.attack(entity)
        if isinstance(entity, Equipment):
            if isinstance(entity,Potion):
                self.add_to_inventory(entity)
                self.heal()
                self.map.entities.remove(entity)
            if isinstance(entity, Coin):
                self.add_coin()
                self.map.entities.remove(entity)
        else:
            return
        
    def add_xp(self, added_xp=1):
        self.xp += added_xp
        self.message_log.add_message(f"XP + {added_xp}",(0, 0, 255))
    
    def level_up(self):
        if self.xp == self.max_xp_per_level:
            self.level += 1
            self.strength += 2
            self.hp = self.max_hp
            self.xp = 0
            self.message_log.add_message(f"player leveled up ! you're at level {self.level}",(0, 0, 255))

    def attack(self, entity):
        entity.attack(self)
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
       
        damage = self.strength - entity.defense
        if entity.hp <= 0:
            self.message_log.add_message(f"Player killed {entity.name}", (0,255,0))
            entity.dies()
            self.add_xp(entity.added_xp)
            

        elif damage > 0 and self.attack_cooldown == 0:
            self.message_log.add_message(f"{self.name} attacks {entity.name} for {damage} hit points")
            entity.take_damage(damage)
            print("entity hp",entity.hp)
            self.attack_cooldown = 10
            entity.turn = True

    def heal(self):
        if self.hp < self.max_hp: 
            difference = self.max_hp - self.hp
            if difference > 10:
                self.hp += 10
            else:
                self.hp = self.max_hp
            self.message_log.add_message(f"Player used healing potion. {10} HP +10")

    def add_coin(self):
        if self.coin < 10:
            self.coin += 1
            self.message_log.add_message("Player took a coin")
        else:
            self.add_xp()
            self.coin = 0

    def add_to_inventory(self, equipment):
        if len(self.inventory) < self.inventory_size:
            self.inventory.append(equipment)
            self.message_log.add_message(f"{equipment.name} is add to inventory")
    
    def remove_from_inventory(self, equipment):
        if len(self.inventory) == 0:
            return
        self.inventory.remove(equipment)

    def update(self):
        self.level_up()
        self.move()