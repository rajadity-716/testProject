print("Thank you for choosing Python Pizza!")
size=input("What is the size of Pizza you want? S, M or L.\n")
if size.upper()=='S':
    print("Thank you! Small size pizza is $15.")
    cost=15
    want_pep=input("Do you want extra peperonni, extra cost=$2? Y or N.\n")
    if want_pep.upper() =='Y' or want_pep.upper() =='N':
        print("Noted!")
        if want_pep.upper() =='Y':
            cost+=2
    else:
        print("Please enter a correct value. Y or N.")
    
elif size.upper()=='M':
    print("Thank you! Medium size pizza is $20.")
    cost=20
    want_pep=input("Do you want extra peperonni, extra cost=$3? Y or N.\n")
    if want_pep.upper() =='Y' or want_pep.upper() =='N':
        print("Noted!")
        if want_pep.upper() =='Y':
            cost+=3
    else:
        print("Please enter a correct value. Y or N.")
elif size.upper()=='L':
    print("Thank you! Large size pizza is $25.")
    cost=25
    want_pep=input("Do you want extra peperonni, extra cost=$3? Y or N.\n")
    if want_pep.upper() =='Y' or want_pep.upper() =='N':
        print("Noted!")
        if want_pep.upper() =='Y':
            cost+=3
    else:
        print("Please enter a correct value. Y or N.")

    want_cheese=input("Do you want extra cheese on top, extra cost=$1? Y or N.\n")
    if want_cheese.upper() =='Y' or want_cheese.upper() =='N':
        print("Noted!")
        if want_cheese.upper() =='Y':
                cost+=1
    else:
        print("Please enter a correct value. Y or N.")

    print(f"Thank You for placing your order, your total price would be ${cost}.")
else:
    print("Please enter a correct value. S, M or L")







# Y_N_check(var)
# if var =='Y' or var =='N':
#     print("Noted!")
# else:
#     print("Please enter a correct value. Y or N.")