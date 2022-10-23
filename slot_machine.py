import random

MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1

ROWS = 5
COLS = 3

symbol_count = {
    "♠": 2,
    "♥": 4,
    "♦": 6,
    "♣": 8,
}

symbol_value = {
    "♠": 5,
    "♥": 4,
    "♦": 3,
    "♣": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    print("\nHere are the results:\n")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="  | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    print("\nWelcome to Roll & Win!")
    while True:
        amount = input("\nHow much would you like to deposit? (mininum amount is $5) $")
        amount.replace(".", "", 1).isdigit()
        
        if amount.isdigit():
            amount = int(amount)
            if amount >= 5:
                break
            else:
                while True:
                    answer = input("\nMinimum amount to deposit is $5. Do you want to continue? (y/n): ").lower()
                    if answer == "y":
                        break
                    elif answer == "n":
                        print("\nThank you for using Roll & Win! Good Bye!\n")
                        quit()
        else:
            print()
            print("\nPlease enter a valid amount to deposit.")
            
    return amount


def get_number_of_lines():
    while True:
        lines = input("\nEnter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("\nEnter a valid number of lines.")
        else:
            print("\nPlease enter a a valid amount.")
    return lines


def get_bet():
    while True:
        amount = input("\nWhat would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"\nAmount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("\nPlease enter a valid amount.")
    return amount   

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"\nYou do not have enough to bet that amount, your current balance is: ${balance}\n")
        else:
            break

    print(f"\nYou are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"\nYou won ${winnings}.")
    print(f"\nYou won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"\nYour current balance is: ${balance}")
        answer = input("\nPress enter to play (e to exit): ")
        if answer == "e":
            break
        balance += spin(balance)

    print(f"\nYou left with ${balance}")


if __name__ == "__main__":
    main()