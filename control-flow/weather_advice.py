def check_weather():
    weather = input("What’s the weather like today? (sunny/rainy/cold): ")
    if weather.lower() == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather.lower() == "rainy":
        print("Wear a t-shirt and sunglasses.Don’t forget your umbrella and a raincoat.")
    elif weather.lower() == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don’t have recommendations for this weather.")    
check_weather()        