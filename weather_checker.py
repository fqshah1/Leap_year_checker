"""Weather Checker: Write a program that asks for the current weather
(sunny, rainy, or cloudy) and prints "It's a good day to go outside"
if the weather is sunny, otherwise print "Stay indoors"""
def weather_check():
#Asks user to input weather status and store the result in weather variable
    weather = input("What is the current Weather? (sunny, rainy, cloudy): ")

    if weather.lower() in ['sunny', 'rainy', 'cloudy']:
        if weather.lower() == "sunny":
            print("It's a good day to go outside!")
        else:
            print("Stay indoors!")
    else:
        print("Invalid input. Please try again.")

p_weather_check = weather_check()
print(p_weather_check)
