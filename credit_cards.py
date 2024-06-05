import random

def credit_card(number_of_cards):
    for _ in range(number_of_cards):
        credit_card = []
        first_four = []
        second_four = []
        third_four = []
        last_four = []
        for n in range(4):
            first_four.append(str(random.randint(0, 9)))
        for n in range(4):
            second_four.append(str(random.randint(0, 9)))
        for n in range(4):
            third_four.append(str(random.randint(0, 9)))
        for n in range(4):
            last_four.append(str(random.randint(0, 9)))

        first_four.append("-")
        second_four.append("-")
        third_four.append("-")

        credit_card = first_four + second_four + third_four + last_four
        print("".join(credit_card))

def main():
    number_of_cards = int(input("How many credit cards would you like to generate? "))
    credit_card(number_of_cards)

main()