#Functions:
def Y_N_check(var):
    if var =='Y' or var =='N':
        print("Noted!")
        return var #returning Yes or No
    else:
        print("Please enter a correct value. Y or N.")

def taking_size_input(var):
    fsize=input(f"What is the size of {var} you want? S, M or L.\n")
    fsize=fsize.upper()
    return(fsize)

def taking_oth_input(var,inc):
   
    add_cost=0
    want=input(f"Do you want extra {var}, extra cost=${inc}? Y or N.\n")
    want=want.upper()
    #print (f"want={want}")
    
    fwant=Y_N_check(want)
    #print (f"fwant={fwant}")
    
    if fwant=='Y':
        add_item="Y"
        add_cost+=inc
        print(f"additional_cost=${add_cost}")
    else:
        add_item="N"
    return add_cost,add_item

def recheck():
    check=input("Would you like to place the order? Y-yes,N-no.")
    check=check.upper()
    fcheck=Y_N_check(check)
    return fcheck

def start():
    size=taking_size_input("pizza")

    if size=='S':
        print("Thank you! Small size pizza is $15.")
        cost=15
        pep_cost=2
        che_cost=1
        extracost_pep,extra_item1=taking_oth_input("peperonni",pep_cost)
        if extra_item1=="N":
            extra_item1="no"
        else:
            extra_item1=""
        print(extracost_che)
        cost+=int(extracost_che)
        print(extracost_pep)
        cost+=int(extracost_pep)
        extracost_che,extra_item2=taking_oth_input("cheese",che_cost)
        if extra_item2=="N":
            extra_item2="no"
        else:
            extra_item2=""
        print(extracost_che)
        cost+=int(extracost_che)


    elif size=='M':
        print("Thank you! Medium size pizza is $20.")
        cost=20
        pep_cost=3
        che_cost=1
        extracost_pep,extra_item1=taking_oth_input("peperonni",pep_cost)
        if extra_item1=="N":
            extra_item1="no"
        else:
            extra_item1=""
        print(extracost_che)
        cost+=int(extracost_che)

        print(extracost_pep)
        cost+=int(extracost_pep)
        extracost_che,extra_item2=taking_oth_input("cheese",che_cost)
        if extra_item2=="N":
            extra_item2="no"
        else:
            extra_item2=""
        print(extracost_che)
        cost+=int(extracost_che)

    elif size=='L':
        print("Thank you! Large size pizza is $25.")
        cost=25
        pep_cost=3
        che_cost=1
        extracost_pep,extra_item1=taking_oth_input("peperonni",pep_cost)
        if extra_item1=="N":
            extra_item1="no extra"
        else:
            extra_item1=""
        cost+=int(extracost_pep)
        extracost_che,extra_item2=taking_oth_input("cheese",che_cost)
        if extra_item2=="N":
            extra_item2="no extra"
        else:
            extra_item2=""
        cost+=int(extracost_che)
    else:
        print("Please enter a correct value. S, M or L")

    print(f"Thank You for placing your order, your item would be {size} size Pizza with {extra_item1} peperroni and {extra_item2} cheese. Total price would be ${cost}.")
    re=recheck()
    if re=="Y":
        print("Thanks! Have a great Day!")
    else:
        cost,size,extra_item1,extra_item2=start()

    return cost,size,extra_item1,extra_item2

print("Thank you for choosing Python Pizza!")
cost,size,extra_item1,extra_item2=start()