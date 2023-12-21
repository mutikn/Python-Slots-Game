import random
import data


def check_the_winnig(columns, lines, bet1, value):
    winniggs = 0
    winnigg_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns :
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winniggs += value[symbol] * bet1
            winnigg_lines.append(line + 1)

    return winniggs, winnigg_lines


def spin_the_slots(rows, cols, symbols):
    list_of_symbols = []
    for symbol, symbol_counts in symbols.items():
        for _ in range(symbol_counts):
            list_of_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        new_symbols = list_of_symbols[:]
        for _ in range(rows):
            value = random.choice(new_symbols)
            new_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_the_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end='|')
            else:
                print(column[row], end='')
        print()


def deposit():
    while True:
        money = input("Введите взнос:$ ")
        if money.isdigit():
            if int(money) > 0:
                break
            else:
                print(f'Ваш взнос должен быть больше 0')
        else:
            print("Введите целое число")

    return money


def get_number_of_lines():
    while True:
        number_of_lines = input(f"Введите количество слотов {1}-{3} : ")
        if number_of_lines.isdigit():
            if 1 <= int(number_of_lines) <= data.MAX_LINES:
                break
            else:
                print(f'Количество слотов должно быть от 1 до 3')
        else:
            print("Введите целое число")

    return number_of_lines


def bet():
    while True:
        amount_of_bet_for_one_line = input(f"Введите ставку на 1 слот ")
        if amount_of_bet_for_one_line.isdigit():
            if data.MIN_BET <= int(amount_of_bet_for_one_line) <= data.MAX_BET:
                break
            else:
                print(f'Количество должно быть от {data.MIN_BET}$ до {data.MAX_BET}$')
        else:
            print("Введите целое число")

    return amount_of_bet_for_one_line


def do_you_want_to_spin():
    question = input("Крутить? Да/Нет: ")
    return question


def do_you_want_to_quit():
    question2 = input("Вы хотите выйти ? Да/Нет: ")
    return question2


def run():
    new_deposit = 0
    amount_of_money = int(deposit())
    number_of_lines = int(get_number_of_lines())
    while True:
        amount_of_bet = int(bet())
        total_bet = amount_of_bet * number_of_lines
        if total_bet > amount_of_money:
            print(f"Ваш взнос больше вашего депозита, ваш баланс составляет {amount_of_money}$ ")
        else:
            break
    print(f'Ваша ставка {amount_of_bet}$ на {number_of_lines}. Общая ставка составляет {total_bet}$')

    while True:
        answer = do_you_want_to_spin()
        if answer == 'Да':
            slots = spin_the_slots(data.ROWS, data.COLS, data.symbol_count)
            print_the_machine(slots)
            winnig, winnigs_lines = check_the_winnig(slots, number_of_lines, amount_of_bet, data.symbol_value)
            print(f'Вы выиграли {winnig}$')
            print(f'На линии', *winnigs_lines )
            new_deposit = winnig - total_bet
            break
        else:
            answer2 = do_you_want_to_quit()
            if answer2 == "Да":
                break
    return new_deposit

if __name__ == '__main__':
    while True:
        spin = input("Вы хотите продолжить? Да/Нет ")
        if spin == "Да":
            run()
        else:
            break

