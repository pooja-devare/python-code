
# x is the variable to match
match px:
    # if x is 0
    case 0:
        print("x is zero")

    # if x is not 90
    case _ if px != 90:
        print(px, "is not 90")
        
    # if x is not 80
    case _ if px != 80:
        print(px, "is not 80")
        
    # for any other value of x
    case _:
        print(px)