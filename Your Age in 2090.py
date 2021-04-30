# Your age in 2090

today = 2021
hundfromToday = today + 100

def age(userAge):
    userAge = int(userAge)
    if userAge<1:
        print("\nYou are not born yet!!\n")
    elif userAge>100:
        print("\nYou seem to be the oldest person alive!!\n")
    else:
        print(f"\nYou will turn 100 in {hundfromToday-userAge}.")
    
def year(userBirth):
    userBirth = int(userBirth)
    if userBirth>today:
        print("\nYou are not born yet!!\n")
    elif (userBirth+100)<=today:
        print("\nYou seem to be the oldest person alive!!\n")
    else:
        print(f"\nYou will turn 100 in {userBirth+100}.")

while True:
    userAge = input("\nEnter you Age or Year of birth\n: ")
    partYearChoice = input("Want to see your age in that particular year?\n\t1. No\n\t2. Yes\n: ")
    if partYearChoice=="1":
        if len(userAge)==4:
            userAge = int(userAge)
            year(userAge)
            break

        elif len(userAge)==2 or int(userAge)==100:
            userAge = int(userAge)
            age(userAge)
            break

        else:
            print("\nNeither a year of birth or your age. Please enter it again!\n")
            continue

    elif partYearChoice=="2":
        viewAgeYear = int(input("\nEnter year\n: "))
        if len(userAge)==4:
            userAge = int(userAge)
            year(userAge)
            age_in_year = viewAgeYear-userAge
            print(f"\nYour age in year {viewAgeYear} will be {age_in_year} years.\n")
            break

        elif len(userAge)==2 or int(userAge)==100:
            userAge = int(userAge)
            age(userAge)
            age_in_year = (viewAgeYear-today)+userAge
            print(f"\nYour age in year {viewAgeYear} will be {age_in_year} years.\n")
            break

        else:
            print("\nNeither a year of birth or your age. Please enter it again!\n")
            continue

    else:
        print("\nInvalid Input!\n")
        continue