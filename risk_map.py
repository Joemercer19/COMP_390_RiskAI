from Territory import Territory

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

        self.territories[territory_a].add_neighbor(territory_b)
        self.territories[territory_b].add_neighbor(territory_a)  