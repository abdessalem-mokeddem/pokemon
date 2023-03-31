import random
import time

class Pokemon:
    def __init__(self, name, type1, type2=None):
        self.__name = name
        self.__type1 = type1
        self.__type2 = type2
        self.__max_hp = 100
        self.__hp = self.__max_hp
        self.__level = 1
        self.__attack_power = 0
        self.__defense = 0

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_max_hp(self):
        return self.__max_hp

    def get_level(self):
        return self.__level

    def get_type1(self):
        return self.__type1

    def get_type2(self):
        return self.__type2

    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power

    def set_defense(self, defense):
        self.__defense = defense

    def display_info(self):
        print(f"{self.__name} (level {self.__level}) - {self.__hp}/{self.__max_hp} HP")
        print(f"Type: {self.__type1}")
        if self.__type2:
            print(f"Type: {self.__type2}")
        print(f"Attack Power: {self.__attack_power}")
        print(f"Defense: {self.__defense}")

from pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Normal")
        self.set_attack_power(10)
        self.set_defense(5)
        self.__max_hp = 120
        self.__hp = self.__max_hp

class Fire(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Fire")
        self.set_attack_power(15)
        self.set_defense(3)
        self.__max_hp = 90
        self.__hp = self.__max_hp

class Water(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Water")
        self.set_attack_power(12)
        self.set_defense(4)
        self.__max_hp = 100
        self.__hp = self.__max_hp

class Earth(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Earth")
        self.set_attack_power(8)
        self.set_defense(8)
        self.__max_hp = 150
        self.__hp = self.__max_hp

from types import Normal, Fire, Water, Earth

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
    
    def check_faint(self):
        if self.pokemon1.current_health <= 0:
            return self.pokemon2.name
        elif self.pokemon2.current_health <= 0:
            return self.pokemon1.name
        else:
            return None
    
    def get_winner(self):
        return self.check_faint() or "Tie"
    
    def get_damage_multiplier(self, attacking_type, defending_type):
        if attacking_type == "Feu":
            if defending_type == "Eau":
                return 0.5
            elif defending_type == "Plante":
                return 2
            else:
                return 1
        elif attacking_type == "Eau":
            if defending_type == "Plante":
                return 0.5
            elif defending_type == "Feu":
                return 2
            else:
                return 1
        elif attacking_type == "Plante":
            if defending_type == "Feu":
                return 0.5
            elif defending_type == "Eau":
                return 2
            else:
                return 1
        else:
            return 1
    
    def apply_damage(self, damage, target):
        defense_multiplier = target.defense / 100
        type_multiplier = self.get_damage_multiplier(self.pokemon1.type, target.type)
        total_damage = damage * defense_multiplier * type_multiplier
        target.current_health -= total_damage
    
    def get_loser(self):
        loser = self.check_faint()
        if loser == self.pokemon1.name:
            return self.pokemon1
        elif loser == self.pokemon2.name:
            return self.pokemon2
        else:
            return None
