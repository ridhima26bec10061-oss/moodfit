
# MODUE 4: OCCASION AND CLOTHING STYLE


def occasion_and_style():
    
    print(" MODULE 4: OCCASION AND CLOTHING")
    

    occasions = [
        "college",
        "casual outing",
        "party",
        "formal event",
        "date",
        "festive event"
]
    styles = [
        "casual",
        "western",
        "traditional",
        "streetwear",
        "formal",
        "minimal"
]

    
    #OCCASION
    

    print("\nSelect the occasion:")
    for i in range(len(occasions)):
        print(i+1, ".", occasions[i])

    while True:
        choice = input("Enter your choice (1-6): ")
        if choice.isdigit():

            choice = int(choice)
            if 1 <= choice <= len(occasions):
                selected_occasions = occasions[choice - 1]
                break
            print("Invalid choice. Please select a number from 1 to 6.")

    
    #CLOTHING STYLE
    

    print("\nSelect your preferred clothing style:")
    for i in range(len(styles)):
        print(i+1, ".", styles[i] )

    while True:
        choice = input("Enter your choice (1-6): ")
        if choice.isdigit():
            choice = int(choice)
            
            if 1 <= choice <= len(styles):
             selected_style = styles[choice - 1]
             break
        print("Invaalid choice. Please select a number from 1 to 6")
    return selected_occasions, selected_style
                
