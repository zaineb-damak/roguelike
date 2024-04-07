# player.py

import pygame
from creature import Creature
from monster import Monster
from equipment import Equipment, Potion, Coin, Weapon, Armor


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
        self.using_armor = False
        self.using_weapon = False
        self.active_weapon = None
        self.active_armor = None
        

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
            if self.using_armor :
                self.use_equipment(self.active_armor)
            if self.using_weapon:
                self.use_equipment(self.active_weapon)
        if isinstance(entity, Equipment):
            if isinstance(entity, Coin):
                self.add_coin()
                self.map.entities.remove(entity)
                self.map.equipments.remove(entity)
            else:
                self.add_to_inventory(entity)
                print(self.inventory)
               
                    
        else:
            return
        
    def add_xp(self, added_xp=1):
        self.xp += added_xp
        self.message_log.add_message(f"XP + {added_xp}",(0, 0, 255))
    
    def level_up(self):
        if self.xp >= self.max_xp_per_level:
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
            self.message_log.add_message(f"Player used healing potion. HP +10")
    
    def equip(self, equipment):
        if isinstance(equipment, Weapon):
            if self.active_weapon is None:
                self.active_weapon = equipment
                self.using_weapon = True
                self.strength += equipment.extra_strength
                self.message_log.add_message(f"Player is equipped with a weapon. strength +{equipment.extra_strength}")
        if isinstance(equipment, Armor):
            if self.active_armor is None:
                self.active_armor = equipment
                self.using_armor = True
                self.defense += equipment.extra_defense
                self.message_log.add_message(f"Player is equipped with a armor. strength +{equipment.extra_defense}")
    
    def unequip(self, equipment):
        self.remove_from_inventory(equipment)
        
        if isinstance(equipment, Weapon):
            self.active_weapon = None
            self.using_weapon = False
            self.strength -= equipment.extra_strength
        if isinstance(equipment, Armor):
            self.active_armor = None
            self.using_armor = False
            self.defense -= equipment.extra_defense

    def use_equipment(self, equipment):
        if equipment is not None:
            equipment.usage_count += 1
            self.message_log.add_message(f"Player used a {equipment.name}. Player can use the {equipment.name} {equipment.max_usage_count - equipment.usage_count} more times")
            if equipment.usage_count >= equipment.max_usage_count:
                self.unequip(equipment)
        return

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
            self.map.entities.remove(equipment)
            self.map.equipments.remove(equipment)
            self.message_log.add_message(f"{equipment.name} is added to inventory")
        return
    
    def remove_from_inventory(self, equipment):
        if len(self.inventory) == 0:
            return
        self.inventory.remove(equipment)
    
    def use_item(self,num):
        if len(self.inventory) == 0 or num >= len(self.inventory):
            return
        if self.inventory[num] is not None:
            if isinstance(self.inventory[num], Potion):
                self.heal()
            elif isinstance(self.inventory[num], Weapon) or isinstance(self.inventory[num], Armor):
                self.equip(self.inventory[num])
                return
            else:
                return
            self.remove_from_inventory(self.inventory[num])

    def update(self):
        self.level_up()
        self.move()