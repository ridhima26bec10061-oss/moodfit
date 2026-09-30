#MODULE 2: MOOD SELECTION


def mood_selection():

    
    print(" \n MODULE 2: MOOD")
    

    moods = [
        "happy",
        "chill",
        "romantic",
        "confident",
        "energetic",
        "cozy",
        "sexy"
        ]

    print("\nSelect your current mood:")

    for i in range(len(moods)):
        print(i + 1, ".", moods[i])
    while True:
        choice = input("Enter your chcoice (1-7): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(moods):
                return moods[choice - 1]
        print("Invalid choice. Please select a number 1 to 7.")
