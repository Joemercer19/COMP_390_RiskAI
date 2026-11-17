import random

class CombatSystem:
    def roll_dice(self, number_of_dice):
        rolls = []

        for _ in range(number_of_dice):
            roll = random.randint(1,6)
            rolls.append(roll)

        rolls.sort(reverse=True)
        return rolls

    def get_attacker_dice(self, armies):
        if armies <=1:
            return 0
        return min(3, armies - 1)

    def get_defender_dice(self, armies):
        return min(2, armies)

    def compare_rolls(self, attacker_rolls, defender_rolls):
        attacker_losses = 0
        defender_losses = 0
        comparisons = min(len(attacker_rolls), len(defender_rolls))
        for i in range(comparisons):
            if attacker_rolls[i] > defender_rolls[i]:
                defender_losses += 1
            else:
                attacker_losses += 1
        return attacker_losses, defender_losses

    def resolve_combat(self, attacker, defender):
        if attacker.owner_id is None or defender.owner_id is None:
            raise ValueError("Both territories must have an owner before combat.")
        if defender.armies <= 0:
            raise ValueError("Defending territory must have at least 1 army")

        if attacker.armies <= 1:
            raise ValueError("Attacking territory must have at least 2 armies.")
        if attacker.owner_id == defender.owner_id:
            raise ValueError("A player cannot attack their own territory.")

        if defender.name not in attacker.neighbours:
             raise ValueError("Attacking and defending territories must be neighbours.")

        attacker_dice = self.get_attacker_dice(attacker.armies)
        defender_dice = self.get_defender_dice(defender.armies)

        attacker_rolls = self.roll_dice(attacker_dice)
        defender_rolls = self.roll_dice(defender_dice)

        attacker_losses, defender_losses = self.compare_rolls(
                attacker_rolls,
                defender_rolls
            )

        attacker.armies -= attacker_losses
        defender.armies -= defender_losses

        captured = False

        if defender.armies == 0:
            defender.owner_id = attacker.owner_id

        armies_to_move = attacker_dice

        attacker.armies -= armies_to_move
        defender.armies = armies_to_move

        captured = True

        return (attacker_rolls, defender_rolls, attacker_losses, defender_losses, captured)