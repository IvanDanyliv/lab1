#!/usr/bin/python3

def print_numbers(numbers):
    print "Telephone Numbers and Names:"
    for x in numbers.keys():
        print "Name:", x, "\tNumber:", numbers[x]
    print

def add_number(numbers, name, number):`
    numbers[name] = number

def load_numbers(numbers, filename):
    in_file = open(filename, "r")
    for in_line in in_file:
        in_line = in_line.rstrip('\n')        
        name, number = in_line.split(",")
        numbers[name] = number
    in_file.close()

def save_numbers(numbers, filename):
    out_file = open(filename, "w")
    for x in numbers.keys():
        out_file.write(x + "," + numbers[x] + "\n")
    out_file.close()

def search_number(numbers, name):
    if name in numbers:
        return "The number is " + numbers[name]
    else:
        return name + " was not found"

def print_menu():
    print '1. Print Phone Numbers and Names'
    print '2. Add a Phone Number'
    print '3. Load numbers'
    print '4. Save numbers'
    print '5. Search a phone number'
    print '6. Quit'
    print

phone_list = {}
menu_choice = 0
print_menu()
while True:
    menu_choice = input("Type in a number: ")
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print "Add Name and Number"
        name = raw_input("Name: ")
        phone = raw_input("Number: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        filename = raw_input("Filename to load: ")
        load_numbers(phone_list, filename)
    elif menu_choice == 4:
        filename = raw_input("Filename to save: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 5:
        print "Search Number"
        name = raw_input("Name: ")
        print search_number(phone_list, name)
    elif menu_choice == 6:
        break
    else:
        print_menu()
