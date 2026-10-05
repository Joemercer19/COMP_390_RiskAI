from Territory import Territory
from risk_map import RiskMap

game_map = RiskMap()

game_map.add_territory("Alaska", "North America")
game_map.add_territory("Alberta", "North America")

game_map.connect("Alaska", "Alberta")

alaska = game_map.get_territory("Alaska")

print(alaska) 
print(alaska.neighbours) 

alaska = game_map.get_territory("Alaska")
alberta = game_map.get_territory("Alberta")

alaska.owner_id = 1
alberta.owner_id = 1

player_one_territories = game_map.get_owned_territories(1)
for territory in player_one_territories:
    print(territory)