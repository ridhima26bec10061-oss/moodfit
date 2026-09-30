# MODULE 3: WEATHER SELECTION

def weather_selection():
    print("\n MODULE 3: WEATHER")

    weather = [
        " hot",
        "warm",
        " chilly",
        " rainy"
    ]

    print("\nSelect the current weather:")

    for i in range(len(weather)):
        print(i + 1, ".", weather[i])

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(weather):
                return weather[choice - 1]

        print("Invalid choice. Please select a number from 1 to 4.")
