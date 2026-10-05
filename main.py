from Territory import Territory
from risk_map import RiskMap
alaska = Territory("Alaska", "North America")
alaska.add_neighbor("Alberta")
alaska.add_neighbor("Kamchatka")



game_map = RiskMap()

game_map.add_territory("Alaska", "North America")
game_map.add_territory("Alberta", "North America")

game_map.connect("Alaska", "Alberta")

print(game_map.territories["Alaska"].neighbors)
print(game_map.territories["Alberta"].neighbors)


