from risk_map import RiskMap
from player import player
from combat import CombatSystem
import random


class Game:
    def __init__(self):
        self.risk_map = RiskMap()
        self.combat = CombatSystem()

        self.players = [
            player(1, "Player 1", "red"),
            player(2, "Player 2", "blue")
        ]

        self.current_player_index = 0
        self.turn_number = 1
    def get_current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        self.current_player_index = 1 - self.current_player_index

    def end_turn(self):
        self.turn_number += 1
        self.next_player()

    def setup_test_map(self):
        self.risk_map.add_territory("Alaska", "North America")
        self.risk_map.add_territory("Alberta", "North America")
        self.risk_map.add_territory("Kamchatka", "Asia")
        self.risk_map.add_territory("Ontario", "North America")

        self.risk_map.connect("Alaska", "Alberta")
        self.risk_map.connect("Alaska", "Kamchatka")
        self.risk_map.connect("Alberta", "Ontario")

    def assign_test_territories(self):
        territories = list(self.risk_map.territories.values())
        random.shuffle(territories)

        for index, territory in enumerate(territories):
            player = self.players[index % len(self.players)]
            territory.owner_id = player.player_id

    def place_initial_test_armies(self):
        for territory in self.risk_map.territories.values():
            territory.armies = 1

    def setup_game(self):
        self.setup_test_map()
        self.assign_test_territories()
        self.place_initial_test_armies()
        self.assign_starting_armies()
        self.place_starting_reserves()

    def assign_starting_armies(self):
        starting_armies = 40

        for player in self.players:
            owned_territories = player.get_territories(self.risk_map)
            deployed_armies = len(owned_territories)

            player.reserve_armies = starting_armies - deployed_armies
   
    def place_starting_reserves(self):
        for player in self.players:
            owned_territories = player.get_territories(self.risk_map)

            territory_index = 0

            while player.reserve_armies > 0:
                territory = owned_territories[territory_index]

                territory.armies += 1
                player.reserve_armies -= 1

                territory_index = (territory_index + 1) % len(owned_territories)

    def calculate_reinforcements(self, player):
        territories_owned = len(player.get_territories(self.risk_map))

        reinforcements = max(3, territories_owned // 3)

        return reinforcements

    def give_reinforcements(self, player):
        reinforcements = self.calculate_reinforcements(player)

        player.reserve_armies += reinforcements

        return reinforcements