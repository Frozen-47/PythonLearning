data = input("Enter Signal : ")
match data:
    case "RED":
        print("Stop")
    case "YELLOW":
        print("Ready")
    case "GREEN":
        print("Go")
    case _ :
        print("Invalid")
