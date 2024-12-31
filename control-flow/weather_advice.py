Weather = input("What's the weather like today?(sunny/rainy/cold): " )
if Weather == "sunny":
    message = "Wear a t-shirt and sunglasses."
elif Weather == "rainy":
    message = "Don't forget your umbrella and raincoat."
elif Weather == "cold":
    message = "Make sure to wear a long coat and a scarf."
else :
    message = "Sorry, I don't have recommendations for this weather"
print(message)
