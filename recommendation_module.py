
#MODULE 5: COMBINED FASHIO RECOMMENDATION
def generate_recommendation(
    name,
    age,
    mood,
    weather,
    occasion,
    style):

    # DEFAULT VARIABLES

    outfit = ""
    footwear = ""
    accessories = ""
    colours = ""
    styling_tip = ""
    reason = ""

    # MOOD-BASED RECOMMENDATION

    if mood == "happy":

        outfit = "bright coloured top with comfortable jeans"
        footwear = "white sneakers"
        accessories = "colourful bracelet or watch"
        colours = "Yellow, white, pink or light blue"
        styling_tip = "Add a colourful accessory to make the outfit lively."
        reason = "cour happy mood matches bright and cheerful colours"

    elif mood == "chill":

        outfit = "Oversized t-shirt with relaxed-fit jeans"
        footwear = "Casual sneakers"
        accessories = "Simple watch or bracelet"
        colours = "White, grey, beige or pastel shades"
        styling_tip = "Keep the outfit comfortable and relaxed."
        reason = "Your chill mood matches a comfortable and effortless outfit"

    elif mood == "confident":

        outfit = "well-fitted top with straight-fit jeans or trousers"
        footwear = "clean sneakers or boots"
        accessories = "watch and one statement accessory"
        colours = "black, white, navy or deep red"
        styling_tip = "Keep the outfit clean and structured."
        reason = "Your confident mood matches a strong and well-balanced outfit"

    elif mood == "romantic":

        outfit = "elegant top with trousers, skirt or a simple dress"
        footwear = "flats, sandals or clean sneakers"
        accessories = "small earrings or delicate bracelet"
        colours = "pink, cream, white, lavender or pastel shades"
        styling_tip = "use soft colours and simple accessories"
        reason = "your romantic mood matches soft and elegant styling"

    elif mood == "energetic":

        outfit = "Graphic t-shirt with cargo pants or comfortable jeans"
        footwear = "Sporty sneakers"
        accessories = "Cap, watch or simple bracelet"
        colours = "Red, blue, black or bright colours"
        styling_tip = "Choose comfortable clothes that allow easy movement."
        reason = "Your energetic mood matches sporty and practical clothing."

    elif mood == "COSY":

        outfit = "Simple cotton top with relaxed trousers or jeans"
        footwear = "Comfortable sneakers or sandals"
        accessories = "Minimal bracelet or watch"
        colours = "White, beige, light blue, green or pastel shades"
        styling_tip = "Keep the overall look simple and comfortable."
        reason = "Your calm mood matches soft colours and minimal styling"

    # WEATHER ADJUSTMENT

    if weather == "Hot":

        outfit = outfit + " Made from light and breathable fabric."
        footwear = footwear + " Suitable for warm weather."

    elif weather == "Warm":

        outfit = outfit + " Using comfortable and breathable clothing."
        footwear = footwear + " Suitable for a warm day."

    elif weather == "Chilly":

        outfit = outfit + " With a jacket, sweater or hoodie."
        footwear = footwear + " Suitable for colder weather."

    elif weather == "Rainy":

        outfit = outfit + " With a light waterproof layer."
        footwear = "Water-resistant shoes or sneakers"

    # OCCASION ADJUSTMENT

    if occasion == "College":

        styling_tip = styling_tip + \
                      " Keep the outfit practical and comfortable for college."

    elif occasion == "Casual Outing":

        styling_tip = styling_tip + \
                      " Keep the look relaxed and easy to wear."

    elif occasion == "Party":

        styling_tip = styling_tip + \
                      " Add one stylish statement piece for the party."

    elif occasion == "Formal Event":

        outfit = outfit + " Keep the overall appearance polished and neat."
        footwear = "Formal shoes or clean loafers"
        styling_tip = "Choose simple and elegant accessories."

    elif occasion == "Date":

        styling_tip = styling_tip + \
                      " Keep the outfit neat, comfortable and personal."

    elif occasion == "Festive Event":

        styling_tip = styling_tip + \
                      " Add a traditional or festive accessory"
        
    # CLOTHING STYLE ADJUSTMENT

    if style == "Casual":

        outfit = outfit + " Casual styling is recommended."

    elif style == "Western":

        outfit = outfit + " Use a modern western styling approach."

    elif style == "Traditional":

        outfit = outfit + \
                 " Add a traditional element such as a kurta, ethnic print or traditional accessory."

    elif style == "Streetwear":

        outfit = outfit + \
                 " Add streetwear elements such as an oversized layer or cargo-style clothing."

    elif style == "Formal":

        outfit = outfit + \
                 " Keep the clothing structured and formal."

    elif style == "Minimal":

        outfit = outfit + \
                 " Keep the look clean with minimal patterns and accessories."

    # FINAL RESULT

    print("\n")
    print("              YOUR MOODFIT RESULT")

    print("\nUser Information")
    print("Name:", name)
    print("Age:", age)

    print("\nYour Selections")
    print("Mood:", mood)
    print("Weather:", weather)
    print("Occasion:", occasion)
    print("Clothing Style:", style)

    print("\nYour Fashion Recommendation")
    print("Outfit:", outfit)
    print("Footwear:", footwear)
    print("Accessories:", accessories)
    print("Suggested Colours:", colours)
    print("Styling Tip:", styling_tip)

    print("\nWhy this recommendation?")
    print(reason)

    print("          Thank you for using MoodFit!")
