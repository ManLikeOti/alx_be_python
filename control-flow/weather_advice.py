weather = input("What's the weather like today? (sunny/rainy/cold): " ).lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif weather == "cold":
    print("Make sure to wear a long coat and a scarf.")
else :
    print("Sorry, I don't have recommendations for this weather")