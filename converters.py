def converters():
    print('sample conveter')
    def sample():
        print('''choose any one of the following
        1.kg to lbs
        2.lbs to kg
        3.inches to cm
        4.cm to inches
        5.cm to feet
        6.feet to cm
        7.quit''')
    sample()
    while True :
        choice = input('')
        if choice == '1':
            weight = float(input("Enter weight in kilo grams: "))
            weight = weight / 0.453
            print(f'{weight} pounds \n')
            sample()
        elif choice == '2':
            weight =float(input("Enter weight in pounds: " ))
            weight = weight * 0.453
            print(f'{weight} kilos \n')
            sample()
        elif choice == '3':
            height = float(input('Enter your height in inches: '))
            height = height * 2.54
            print(f'{height} centimeters \n ')
            sample()
        elif choice == '4':
            inches = float(input('Enter your height in centimeters: '))
            inches = inches / 2.54
            print(f'{inches} inches \n')
            sample()
        elif choice == '6':
            print('Enter your height in feet and inches seperately: ')
            feet = float(input('Feet = '))
            inches = float(input('Inches = '))
            tot_height = feet * 30.48 + inches * 2.54
            print(f'{tot_height} centimeters \n')
            sample()
        elif choice == '5':
            height= float(input('Enter your height in centimeters: '))
            height1 = height * 0.0328 #this logic is fine but not complete
            height2 = height * 0.394  #this one too
            inches = round(height2,2)
            feet = round(height1,2)
            print(f'''{feet}' {inches}" ''')
            print("Option 5 still in devlopment, so gives two values in both feet and inches")
            sample()
        elif choice == '7':
            break
        else :
            print(" Invalid choice! Try Again ")
            sample()
print("program completed")
