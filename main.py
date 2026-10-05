from Territory import Territory
alaska = Territory("Alaska", "North America")
alaska.add_neighbor("Alberta")
alaska.add_neighbor("Kamchatka")

print(alaska)
print(alaska.neighbors)
print(alaska.is_owned_by(1))  # False

