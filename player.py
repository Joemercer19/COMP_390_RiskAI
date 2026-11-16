class player:

    def __init__(self, player_id, name, colour):
        self.player_id = player_id
        self.name = name
        self.colour = colour
        self.reserve_armies = 0
    def get_territories(self, risk_map):
        return risk_map.get_owned_territories(self.player_id)

    def get_total_armies(self, risk_map):
        territories = self.get_territories(risk_map)

        total = 0

        for territory in territories:
            total += territory.armies

        return total

    def is_eliminated(self, risk_map):
        return len(self.get_territories(risk_map)) == 0

    def __str__(self):
        return f"{self.name}| Player {self.player_id} | Colour {self.colour}"