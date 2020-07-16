"""
Author  : Vivek Shinde
Date    : 15/06/2020
purpose : Practice problem solving
code    : Ankit's fraud multiplication table

"""
import random


def ankit_multiplication(num):
    for table in range(1, 11):
        x = num * table
        ankit_list.append(x)

    wrong_multiplication = random.randrange(1, 9)
    ankit_list[wrong_multiplication] = ankit_list[wrong_multiplication] + 1
    return ankit_list


def is_correct_table(num):
    number = 1
    for x in ankit_list:
        z = num * number
        number += 1
        if x != z:
            print(f'\n\'{x}\' multiplication is wrong')
            print(f"correct multiplication is \"{z}\"")


if __name__ == '__main__':
    ankit_list = []
    ankit_table = int(input('please enter your table : '))
    ankit_multiplication(ankit_table)
    print(ankit_list)

    # check_correct_table = int(input('\nTo check the table : '))
    is_correct_table(ankit_table)

