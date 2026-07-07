# Calculator that save, show, and clear history

# file to save history

file = 'history.txt'

# function to show history

def show_history():
    file_open = open(file , 'r')
    lines = file_open.readlines()

    if (len(lines)==0):
        print('\nNo history found !')
    else:
        for line in lines:
            print()
            print(line.strip())

    file_open.close()

# file to clear history

def clear_history():
    clear = open(file , 'w')
    clear.close()

    print('\nHistory cleared !')

# file to save history

def save_history(equation , output):
    open_file = open(file , 'a')
    open_file.write(equation + '=' + str(output) + '\n')

    print('\nHistory saved.')

    open_file.close()

# file for calculation

import re

def calculation(equation):
    equation = equation.replace(' ' , '')
    splitting = re.split('([+\-*/])' , equation)

    num_1 = float(splitting[0])
    operator = splitting[1]
    num_2 = float(splitting[2])

    if (operator == '+'):
        output = num_1 + num_2
    elif (operator == '-'):
        output = num_1 - num_2
    elif (operator == '*'):
        output = num_1 * num_2
    elif (operator == '/'):
        if num_2 == 0:
            print('\nError! \nDivision by zero not possible')
            return None
        else:
            output = num_1 / num_2
    else:
        print('\nInvalid operator entered. Clculator only supports +,-,*,and /')
        return
    
    print('\nOutput:' , output)
    return output

def main():
    print("\n======Simple Calculator======")

    inpi = ''
    output = None

    while True:
        inp = input('\nEnter command (save,history,clear,exit,calculate): ').lower()
        
        if (inp == 'exit'):
            print("\nCalculator closed.")
            break
        elif (inp == 'calculate'):
            inpi = input('\nEnter equation: ')
            output = calculation(inpi)
        elif (inp == 'save'):
            if output is None:
                print("\nNo calculation to save!")
            else:
                save_history(inpi, output)
        elif (inp == 'history'):
            show_history()
        elif (inp == 'clear'):
            clear_history()


main()
