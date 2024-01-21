
# variable pattern allows user to choose between two different kinds of pattern
# .title() is added, so that whatever the user inputs will correspond to the if statements
pattern = input("You have a choice of two patterns"
                         " that you can choose from.\nThey are:\n\t"
                         " Right Angled Triangle, \n\t"
                         " Isosceles Triangle, \n\t"
                         " Please choose your pattern now: ").title()

# if the user inputs Right Angled Triangle, the following for loop will print the pattern requested
if pattern == "Right Angled Triangle":
    # the user is asked to enter the size that he wants the pattern to be
    size = int(input("Please enter the size that you want"
                     " the triangle to be: "))
    # the user can choose whichever symbol he wants his pattern to be
    symbol = input("Enter a symbol for your triangle: ")
    # We use a nested for loop to print the Right Angled Triangle
    # Firstly, i will loop through variable size. The number of loops is determined by number user inputs
    for i in range(size):
        # the number of times j prints is determined by i.
        # This will continue until i stops looping through size.
        # As i loops, j is looping through i and printing the symbol.
        # The number of times the symbol is printed is dependent on j and the number of times it is looping through i
        # The reason why 1 needs to be added to i, is because i's first loop will be 0.
        # In order for the triangle to be uniform, 1 is added to i for j to print pattern without whitespace
        for j in range(i+1):
            # end=" " needed in order to print the pattern horizontally and not vertically.
            print(symbol, end=" ")
        # closed print statement needed to print pattern correctly
        print()

#  if the user selects Isosceles Triangle, the below will be printed.
elif pattern == "Isosceles Triangle":
    # same variables as above for the user to input the size of the pattern and its symbol
    size = int(input("Please enter the size that you want"
                     " the triangle to be: "))
    symbol = input("Enter a symbol for your triangle: ")

    # i loops through size variable, determined by number user inputs
    for i in range(size):
        # To get an isosceles pattern, we use j to print a blank string
        # j loops through i, size. " " will be printed in a decreasing pattern
        # This creates a 'phantom pattern', creating whitespace to give shape to the isosceles pattern
        for j in range(i, size):
            print(" ", end=" ")
        # j loops through i+1 to get first triangle patter, which will form first half of the isosceles triangle
        for j in range(i+1):
            print(symbol, end=" ")
        # Here, j loops through i without 1 being added in order to remove extra column and to make it uniform
        for j in range(i):
            print(symbol, end=" ")
        # closed print statement needed to print pattern correctly
        print()

else:
    print("Invalid input! ")
