class Territory:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent
        self.owner_id = None
        self.armies = 0
        self.neighbours = set()

    def add_neighbour(self, Territory_name):
        self.neighbours.add(Territory_name)

    def is_owned_by(self, player_id):
        return self.owner_id == player_id

    def __str__(self):
        return (
            f"{self.name} | "
            f"Owner: {self.owner_id} | "
            f"Armies: {self.armies}"    
        )