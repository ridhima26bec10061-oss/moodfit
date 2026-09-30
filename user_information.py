
#MODULE 1: USER INFORMATION


def user_information():

    print("   MODULE 1: USER INFORMATION")

    name = input("Enter your name: ")

    while True:

        age = input("Enter your age: ")

        if age.isdigit():

            age = int(age)

            if age > 0 :
                break

            else:
                print("Please enter a valid age.")
        else:
            print("Please enter age in numbers.")
    return name, age


        

