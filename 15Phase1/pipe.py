day = input("Enter Day : ")
match day:
    case "sunday" | "saturday":
        print(f"{day.capitalize()} is holiday")
    case "wednesday":
        print(f"{day.capitalize()} mid of the day")
    case _:
        print("Remaining days")