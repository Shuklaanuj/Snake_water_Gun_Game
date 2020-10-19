import  random
class SWG_GAME:
    print("Welcome to snake-water-gun game")
    chance = 1
    draw = []
    person = []
    com = []
    while chance<=10:
        n = str(input("Please enter your choice from s w g : \n"))
        m = random.choice(['s','w','g'])
        if m == n.lower():
            draw.append("d")
            print("Match draw ho gya")
        else:
            if m == "s":
                if n == "w":
                    com.append("c")
                    print("Computer is winner")
                else:
                    person.append("p")
                    print("You are winner")
            elif m == "w":
                if n == "g":
                    com.append("c")
                    print("Computer is winner")
                else:
                    person.append("p")
                    print("You are winner")
            else:
                if n == "s":
                    com.append("c")
                    print("Computer is winner")
                else:
                    person.append("p")
                    print("You are winner")
        chance += 1

    print("Computer won {} times ".format(len(com)))
    print("you won {} times ".format(len(person)))
    print("Draw matches {} times".format(len(draw)))
    if len(person)>len(com):
        print("you are winner")
    else :
        print("Well played")