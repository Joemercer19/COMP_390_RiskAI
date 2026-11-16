
from risk_map import RiskMap
from player import player
from combat import CombatSystem

game_map = RiskMap()

game_map.add_territory("Alaska", "North America")
game_map.add_territory("Alberta", "North America")

game_map.connect("Alaska", "Alberta")

alaska = game_map.get_territory("Alaska")
alberta = game_map.get_territory("Alberta")

alaska.owner_id = 1
alberta.owner_id = 2

alaska.armies = 5
alberta.armies = 2

print(alaska)
print(alaska.neighbours)

player_one_territories = game_map.get_owned_territories(1)

for territory in player_one_territories:
    print(territory)


player1 = player(1, "player1", "red")
player2 = player(2, "player2", "blue")


print(player1.player_id)
print(player1.name)
print(player1.colour)
print(player1.reserve_armies)

print(player2.player_id)
print(player2.name)
print(player2.colour)
print(player2.reserve_armies)

player1_territories = player1.get_territories(game_map)
for territory in player1_territories:
    print(territory.name)

print(player1.get_total_armies(game_map))

print(player1.is_eliminated(game_map))

print(player2.is_eliminated(game_map))

combat = CombatSystem()
result = combat.resolve_combat(alaska, alberta)

print(result)

print(alaska)
print(alberta)