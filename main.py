from helpers import diceroller

def main():
    amount = input("Enter number of dice to roll: ")
    sides = input("Enter number of sides on the die: ")
    modifier = input("Enter modifier (default 0): ") or 0
    die = diceroller.Die(int(sides))
    total = die.roll(int(amount), int(modifier))
    if modifier == 0:
        rolledstring = f"{amount}d{sides}"
    elif int(modifier) > 0:
        rolledstring = f"{amount}d{sides}+{modifier}"
    else:
        rolledstring = f"{amount}d{sides}{modifier}"
    print(f"Total roll: {rolledstring} -> {total}")
if __name__ == "__main__":
    main()