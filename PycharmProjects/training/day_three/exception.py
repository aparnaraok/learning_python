while True:
    try:
        x = int(input("Enter a number"))
        break
    except ValueError:
        print ("Oops!That was not a valid number...Try again")