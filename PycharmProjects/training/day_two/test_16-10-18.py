def get_output():
    while True:
        inp = input("Please let me know your input").strip()
        #get_output(inp)
        if (inp == 'yes' or inp == 'YES') or (inp == 'No' or inp == 'NO'):
            print ("The input value entered is correct>>>>>You are in")
            break
        else:
            print ("The input entered is incorrect....Please provide the correct value")

#np = input("Please let me know your input")
get_output()