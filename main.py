
#MOODFIT - MAIN PROGRAM

#Importing functions from all five modules

from user_information import user_information
from mood_module import mood_selection
from weather_module import weather_selection
from clothing_module import occasion_and_style
from recommendation_module import generate_recommendation

#MAIN FUNCTION

def main():

    print("WELCOME TO MOODFIT")
    print("Mood-Based Fashion Recommendation System")

    #MODULE 1
    name, age = user_information()

    #MODULE 2
    mood = mood_selection()

    #MODULE 3
    weather = weather_selection()

    #MODULE 4
    occasion, style = occasion_and_style()

    #MODULE 5
    generate_recommendation(
        name,
        age,
        mood,
        weather,
        occasion,
        style
    )

#PROGRAM START

if __name__ == "__main__":
    main()
