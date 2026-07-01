day = input("Enter Day : ")
match day:
    case "sunday" | "saturday":
        print(f"{day} is holiday")
    case "wednesday":
        print(f"{day} mid of the day")
    case _:
        print("Remaining days")