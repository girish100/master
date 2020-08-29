print("Welcome ")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
energy = int(10)
while age >= 5:
    print("You are eligible to play\nLet's begin\nEnergy = 10")
    print("In the evening you are walking through a forest and you come across a lake")
    choice1 = input('''What will you do
    1.Swim across the lake
    2.Walk around the lake
    3.Go Back
    select your choice 1 or 2 or 3:
    ''')
    if choice1 == '1':
        print("you swim")
        energy -= 5
        print('Energy =', energy)
    elif choice1 == '2':
        print("you walk")
        energy -= 2
        print('Energy = ', energy)
    elif choice1 == '3':
        print("game over")
        break
    else:
        print('Select any one of the above')
    print('''\nIt's already night and you see a house near the lake, what would you do ?\n
        1.Get in the house and take rest
        2.stay by the lake and wait till morning
        3.Go back''')
    choice2 = input("select your choice 1 or 2 or 3: ")
    if choice2 == '1':
        print("You went into the house and took rest")
        energy += 5
        print('Energy = ', energy)
    elif choice2 == '2':
        print("you got cold")
        energy -= 5
        if energy == '0':
            print("Energy = ", energy)
            print("out of energy \nGame over")
            break
        else :
            print("Energy = ", energy)
    elif choice2 == '3':
        print('you got home')
        energy -= 5
        if energy == '0':
            print("Energy = ", energy)
            print("out of energy \nGame over")
            break
        else :
            print("Energy left = ", energy)
        print("Game Over")
        break
    else:
        print("Select any one of the above")
    print('''In the next morning you woke up in the house that you entered last night
    1.Would you like to go back
    2.Continue your journey''')
    choice3 = input("select 1 or 2: ")
    if choice3=='1':
        energy -= 5
        print("You went home\n Energy = ", energy)
        print("Game over")
        break
    elif choice3 == '2':
        print("Thank you ", name)
        print("The game is still under development ")
        break
choice4 = input("would you like to try the converters program\n Type yes/no: " ).lower()
if choice4 == 'yes':
    print("here is a simple converter")
    import converters
    converters.converters()
elif choice4 == 'no':
    print("Thank you")
else :
    print("invaild entry try again")
