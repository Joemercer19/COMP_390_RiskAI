from territory import Territory


class RiskMap:
    def __init__(self):
        self.territories = {}

    def add_territory(self, name, continent):
        if name in self.territories:
            raise ValueError(f"Territory '{name}' already exists on the map.")

        territory = Territory(name, continent)
        self.territories[name] = territory

    def connect(self, territory_a, territory_b):
        if territory_a not in self.territories:
            raise ValueError(f"Territory '{territory_a}' does not exist.")

        if territory_b not in self.territories:
            raise ValueError(f"Territory '{territory_b}' does not exist.")

        self.territories[territory_a].add_neighbour(territory_b)
        self.territories[territory_b].add_neighbour(territory_a)

    def get_territory(self, name):
        if name not in self.territories:
            raise ValueError(f"Territory '{name}' does not exist.")

        return self.territories[name]

    def get_owned_territories(self, player_id):
        owned_territories = []

        for territory in self.territories.values():
            if territory.owner_id == player_id:
                owned_territories.append(territory)

        return owned_territories

    def get_enemy_neighbours(self, territory_name, player_id):
        territory = self.get_territory(territory_name)
        enemy_neighbours = []

        for neighbour_name in territory.neighbours:
            neighbour = self.get_territory(neighbour_name)

            if neighbour.owner_id != player_id:
                enemy_neighbours.append(neighbour)

        return enemy_neighbours
